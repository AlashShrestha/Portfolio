from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "files/index.html")


def resume(request):
    return render(request, "files/resume.html")


def projects(request):
    return render(request, "files/projects.html")


def contact(request):
    return render(request, "files/contact.html")
