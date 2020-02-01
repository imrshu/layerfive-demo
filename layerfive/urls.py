from django.views.generic import TemplateView
from django.urls import path
from .views import CreateUserDescription

app_name = 'layerfive'


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('show', TemplateView.as_view(template_name='show.html'), name='show'),
    path('create', CreateUserDescription.as_view()),
]

