from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post_detail/<int:pk>', views.post_detail, name='post_detail'),
    path('post_creation', views.post_creation, name='post_creation')
]
