from django.shortcuts import render
from courses.models import Course


def search(request):
    if request.method == "GET":
        courses = Course.objects.filter(name__icontains=request.GET['q'])
        context = {
            'courses': courses
        }
        return render(request, 'courses/courses.html', context)
