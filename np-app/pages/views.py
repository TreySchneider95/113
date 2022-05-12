from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from articles.models import Article
from .models import *


class HomeView(ListView):
    template_name = 'home.html'
    model = Article
    context_object_name = 'articles'

class AboutView(TemplateView):
    template_name = 'about.html'