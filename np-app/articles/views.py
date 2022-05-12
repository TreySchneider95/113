from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, RedirectView, TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Article
from .forms import CreateArticle


class AddArticleView(LoginRequiredMixin, CreateView):
    template_name = 'new.html'
    model = Article
    form_class = CreateArticle

class UpdateArticleView(LoginRequiredMixin, UpdateView):
    template_name = 'edit.html'
    model = Article
    form_class = CreateArticle

class DeleteArticleView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'delete.html'

    def get_success_url(self):
        return reverse_lazy('home')

