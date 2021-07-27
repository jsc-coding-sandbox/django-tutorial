from django.shortcuts import render
from django.http import HttpResponse

from .models import Question


def index(request):
    # Get 5 most recent questions (as determined by pub_date)
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # Join them together into a string
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're viewing question %s." % question_id)

def results(request, question_id):
    # No idea why the tutorial does it this way for this one, but I'm copying.
    response = "You're viewing the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
