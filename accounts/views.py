from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from .forms import CreateUserForm

class SignUpView(generic.CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy("accounts:login")
    template_name = "registration/signup.html"
