from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Order, OrderLineItem
from courses.models import Course
from accounts.models import UserProfile
import json
import time


class StripeWebhook_Handler:
    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        customer_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt', {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt', {'order': order})
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )

    def handle_event(self, event):
        return HttpResponse(
            content=f'Webhook Received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(request, self, event):
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        billing_details = intent.charges.data[0].billing_details
        order_total = round(intent.charges.data[0].amount / 100, 2)

        order_exists = False
        profile = UserProfile.objects.get(user=request.user)
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    order_total=order_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook Received: {event["type"]} | SUCCESS: '
                        'Order has been created',
                status=200
            )
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=billing_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(cart).items():
                    course = Course.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        course=course,
                        quantity=item_data,
                    )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook Received: {event["type"]} | ERROR: {e}',
                    status=500
                )
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook Received: {event["type"]} | SUCCESS: '
                    'Order created in webhook',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(
            content=f'Webhook Received: {event["type"]}',
            status=200
        )
