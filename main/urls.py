from django.urls import path
from main.views import HomeTemplateView, NewSingleView


app_name = 'main'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='index'),
    path('single/', NewSingleView.as_view(), name='single'),
]