from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<center><h1>witaj w mojej pizzeri</h1></center>")


def komunikat(request):
    return HttpResponse("<center><h1>Alert RCBG!</h1></center>")


def order(request):
    return HttpResponse("<center><h2>Tutaj zamówisz swoją pitcunie</h2></center>")