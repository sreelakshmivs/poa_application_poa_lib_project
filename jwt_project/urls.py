from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send_jwt/', include('sender_app.urls')),
    path('receive_jwt/', include('receiver_app.urls')),
    path('sender_template/', include('sender_app.urls')),
    path('receiver_template/', include('receiver_app.urls')),  # Add this line
]
