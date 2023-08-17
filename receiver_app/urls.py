from django.urls import path
from . import views

urlpatterns = [
    path('', views.receive_jwt, name='receive_jwt'),
    path('receiver_template/', views.receiver_template_view, name='receiver_template'),
]
