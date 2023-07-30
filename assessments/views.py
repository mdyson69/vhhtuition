from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Assessment, Question
from .forms import AssessmentForm, QuestionForm
from django.contrib.auth.decorators import login_required


def all_assessments(request):
    assessments = Assessment.objects.all().order_by('id')
    context = {
        'assessments': assessments,
    }
    return render(request, 'assessments/assessments.html', context)


def assessment_questions(request, assessment_id):
    assessments = Assessment.objects.filter(id=assessment_id)
    questions = Question.objects.filter(assessment_id=assessment_id)
    context = {
        'assessments': assessments,
        'questions': questions,
    }
    return render(request, 'assessments/assessment_questions.html', context)


@login_required
def assessment_management(request):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page!')
        return redirect(reverse('home'))

    assessments = Assessment.objects.all().order_by('id')
    context = {
        'assessments': assessments,
    }
    return render(request, 'assessments/assessment_management.html', context)


@login_required
def edit_assessment(request, assessment_id):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page!')
        return redirect(reverse('home'))

    assessment = get_object_or_404(Assessment, pk=assessment_id)
    if request.method == 'POST':
        form = AssessmentForm(request.POST, request.FILES, instance=assessment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated assessment')
            return redirect(reverse('assessment_management'))
        else:
            messages.error(
                request, 'Error editing assessment, please check your form and'
                ' try again')
    else:
        form = AssessmentForm(instance=assessment)
    context = {
        'form': form,
        'assessment': assessment,
    }

    return render(request, 'assessments/edit_assessment.html', context)


@login_required
def question_management(request, assessment_id):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page!')
        return redirect(reverse('home'))
    assessments = Assessment.objects.filter(id=assessment_id)
    questions = Question.objects.filter(assessment_id=assessment_id)
    context = {
        'assessments': assessments,
        'questions': questions,
    }
    return render(request, 'assessments/question_management.html', context)


@login_required
def edit_question(request, question_id):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page!')
        return redirect(reverse('home'))

    question = Question.objects.filter(id=question_id).first()
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES, instance=question)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated question')
            return redirect(reverse('assessment_management'))
        else:
            messages.error(
                request, 'Error editing question, please check your form and '
                'try again')
    else:
        form = QuestionForm(instance=question)
    context = {
        'form': form,
        'question': question,
    }

    return render(request, 'assessments/edit_question.html', context)


@login_required
def add_question(request):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added new question!")
            return redirect(reverse('assessment_management'))
        else:
            messages.error(
                request, "Error adding question, please check your form and "
                "try again")
    else:
        form = QuestionForm()

    context = {
        'form': form
    }

    return render(request, 'assessments/add_question.html', context)


@login_required
def delete_question(request, question_id):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page!')
        return redirect(reverse('home'))

    question = Question.objects.filter(id=question_id)
    question.delete()
    messages.success(request, 'Successfully deleted question!')
    return redirect(reverse('assessment_management'))


@login_required
def add_assessment(request):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AssessmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added new assessment')
            return redirect(reverse('assessment_management'))
        else:
            messages.error(
                request, "Error adding question, please check your form and "
                "try again")
    else:
        form = AssessmentForm()
        context = {
            'form': form,
        }

    return render(request, 'assessments/add_assessment.html', context)


@login_required
def delete_assessment(request, assessment_id):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page!')
        return redirect(reverse('home'))

    assessment = get_object_or_404(Assessment, pk=assessment_id)
    assessment.delete()
    messages.success(request, 'Successfully deleted assessment!')
    return redirect(reverse('assessment_management'))
