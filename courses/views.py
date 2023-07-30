from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Course
from .forms import CourseForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def display_courses(request):
    courses = Course.objects.all().order_by('id')
    context = {
        'courses': courses,
    }
    return render(request, 'courses/courses.html', context)


def view_course(request, course_id):
    courses = Course.objects.filter(id=course_id)
    course_object = Course.objects.get(id=course_id)
    course_object.course_views = course_object.course_views+1
    course_object.save()
    context = {
        'courses': courses,
    }
    return render(request, 'courses/view_courses.html', context)


@login_required
def course_management(request):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page!')
        return redirect(reverse('home'))

    courses = Course.objects.all().order_by('id')
    context = {
        'courses': courses,
    }
    return render(request, 'courses/course_management.html', context)


@login_required
def add_course(request):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added new course')
            return redirect(reverse('course_management'))
        else:
            messages.error(
                request, "Error adding question, please check your form and "
                "try again")
    else:
        form = CourseForm()
        context = {
            'form': form,
        }

    return render(request, 'courses/add_course.html', context)


@login_required
def edit_course(request, course_id):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page!')
        return redirect(reverse('home'))

    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated course')
            return redirect(reverse('course_management'))
        else:
            messages.error(
                request, 'Error editing course, please check your form and'
                ' try again')
    else:
        form = CourseForm(instance=course)
    context = {
        'form': form,
        'course': course,
    }

    return render(request, 'courses/edit_course.html', context)


@login_required
def delete_course(request, course_id):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page!')
        return redirect(reverse('home'))

    course = get_object_or_404(Course, pk=course_id)
    course.delete()
    messages.success(request, 'Successfully deleted course!')
    return redirect(reverse('course_management'))
