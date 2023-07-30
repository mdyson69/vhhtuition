from django.shortcuts import get_object_or_404
from courses.models import Course


def cart_contents(request):

    cart_items = []
    total = 0
    course_count = 0
    cart = request.session.get('cart', {})

    for id, quantity in cart.items():
        course = get_object_or_404(Course, pk=id)
        total += quantity * course.price
        course_count += quantity
        cart_items.append({
            'id': id,
            'quantity': quantity,
            'course': course,
        })

    context = {
        'cart_items': cart_items,
        'total': total,
        'course_count': course_count,
    }

    return context
