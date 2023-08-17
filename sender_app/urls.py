
from django.urls import path
from . import views

urlpatterns = [
    path('', views.send_jwt, name='send_jwt'),
    path('sender_template/', views.sender_template_view, name='sender_template'),
]