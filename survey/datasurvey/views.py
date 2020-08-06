from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Question, Choice

# Get question and display them


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list, }

    return render(request, 'datasurvey/index.html', context)


def detail(request, question_id):
    return HttpResponse('You are looking at question %s' % question_id)


def results(request, question_id):
    response = 'You are looking at the results of question %s'
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse('You are voting at question %s' % question_id)
