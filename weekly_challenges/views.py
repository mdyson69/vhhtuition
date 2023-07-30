from django.shortcuts import render


def display_challenges(request):
    return render(request, 'weekly_challenges/challenges.html')
