from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "polls/index.html")

def detail(request, question_id):
    return HttpResponse(f"Você está vendo a questão {question_id}.")

def results(request, question_id):
    return HttpResponse(f"Resultados da questão {question_id}.")

def vote(request, question_id):
    return HttpResponse(f"Votando na questão {question_id}.")