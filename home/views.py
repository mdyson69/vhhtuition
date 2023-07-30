from django.shortcuts import render
from courses.models import Course


def home(request):
    courses = Course.objects.order_by('-course_views')[:3]

    context = {
        'courses': courses,
    }
    return render(request, 'home/index.html', context)


def privacy(request):
    return render(request, 'home/privacy_policy.html')


def cookie(request):
    return render(request, 'home/cookie_policy.html')


def handler_404(request, exception):
    return render(request, '404.html')


def handler_500(request, *args, **argv):
    return render(request, '500.html')
