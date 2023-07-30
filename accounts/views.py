from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from assessments.models import Assessment
from checkout.models import Order
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated')
        else:
            messages.error(request, 'Error updating profile, please check your'
                                    'form and try again.')
    else:
        form = UserProfileForm(instance=profile)

    assessments = Assessment.objects.filter(user=profile)
    orders = profile.orders.all()

    context = {
        'profile': profile,
        'form': form,
        'assessments': assessments,
        'orders': orders,
    }

    return render(request, 'accounts/profile.html', context)


@login_required
def my_courses(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    context = {
        'order': order,
    }
    return render(request, 'checkout/checkout_success.html', context)
