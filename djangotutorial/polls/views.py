#from django.http import Http404
#from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

from .models import Question
from .models import Choice

def detail(request, question_id):
    #try:
    question = get_object_or_404(Question, pk=question_id)
    #except Question.DoesNotExist:
    return render(request,"polls/detail.html", {'question': question})

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date') [:5]
    
    context = {'latest_question_list': latest_question_list,}
    return render(request,'polls/index.html', context)

def results(request, question_id):
    response = "Koukáš na odpovědi na otázku %s."
    return HttpResponse( response % question_id)

def vote(request, question_id):
    return HttpResponse("Hlasuješ k dotazu %s." % question_id)



# Create your views here.
