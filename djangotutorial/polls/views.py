#from django.http import Http404
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
#from django.template import loader
from django.urls import reverse

from .models import Choice, Question


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
    dotaz = get_object_or_404(Question, pk=question_id)
    try:
        sele_choice = dotaz.choice_set.get(pk=request.Post["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": dotaz,
                "error_message": "Nevybral jsi odpověď.",
            },
        )
    else:
        sele_choice.votes = F('votes')+1
        sele_choice.save()
        return HttpResponseRedirect(reverse( 'polls:results', args=(question_id,)))



# Create your views here.
