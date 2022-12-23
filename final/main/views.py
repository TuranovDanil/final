from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
# Create your views here.
from django.views.generic import CreateView


def index(request):
    rec = Product.objects.order_by('name')[:1]
    return render(request, 'main/index.html', {'rec': rec})


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def products(request):
    rec = Product.objects.all()
    return render(request, 'main/products.html', {'rec': rec})


class CreateView(LoginRequiredMixin, CreateView):
    template_name = 'main/create.html'
    model = Product
    login_url = '/login'
    success_url = '/products'
    form_class = CreateForm


class Login(LoginView):
    template_name = 'main/login.html'
    model = User
    success_url = '/'
