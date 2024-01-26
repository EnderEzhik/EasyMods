from django.shortcuts import render


def home(request):
    return render(request, "main/html/home.html")

def addmod(request):
    return render(request, "main/html/addmod.html")