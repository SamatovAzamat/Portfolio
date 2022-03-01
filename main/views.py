from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from main.forms import ContactModelForm
from django.urls import reverse
from main.models import PostModel


class HomeTemplateView(CreateView):
    template_name = 'index.html'
    form_class = ContactModelForm

    def get_success_url(self):
        return reverse('main:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context['posts'] = PostModel.objects.filter(status=PostModel.STATUS_ACTIVE).order_by('-pk')[:3]

        return context


class NewSingleView(TemplateView):
    template_name = 'single.html'

    # def get_success_url(self):
    #     return reverse('main:single.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context['posts'] = PostModel.objects.order_by('-pk').all()

        return context



