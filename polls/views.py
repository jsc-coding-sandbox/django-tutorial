from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    # Get 5 most recent questions (as determined by pub_date)
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
            'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("You're viewing question %s." % question_id)

def results(request, question_id):
    # No idea why the tutorial does it this way for this one, but I'm copying.
    response = "You're viewing the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
