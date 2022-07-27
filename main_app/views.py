from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Comment, Blog, Tags
# Create your views here.

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')