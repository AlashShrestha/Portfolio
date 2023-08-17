from django.urls import path
from project.views import *

urlpatterns = [
    path("", index, name="index"),
    path("resume/", resume, name="resume"),
    path("project/", projects, name="projects"),
    path("contact", contact, name="contact"),
]
