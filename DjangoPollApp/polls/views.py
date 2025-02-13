from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. This is polls index")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id )

def results(request, quesiton_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % quesiton_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
