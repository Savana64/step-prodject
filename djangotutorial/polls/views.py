from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Question
from .models import Choice

def detail(request, question_id):
    return HttpResponse("Koukáš na dotaz %s." % question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date') [:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list,}
    return HttpResponse(template.render(context, request))

def results(request, question_id):
    response = "Koukáš na odpovědi na otázku %s."
    return HttpResponse( response % question_id)

def vote(request, question_id):
    return HttpResponse("Hlasuješ k dotazu %s." % question_id)



# Create your views here.
