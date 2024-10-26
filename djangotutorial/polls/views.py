from django.http import HttpResponse
from django.shortcuts import render

def detail(request, question_id):
    return HttpResponse("Koukáš na dotaz %s." % question_id)

def index(request):
    return HttpResponse("Hello, world. You're at the police roblox.")

def results(request, question_id):
    response = "Koukáš na odpovědi na otázku %s."
    return HttpResponse( response % question_id)

def vote(request, question_id):
    return HttpResponse("Hlasuješ k dotazu %s." % question_id)



# Create your views here.
