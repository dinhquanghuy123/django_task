from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog_views, name='blog'),
    path('blog/details/<int:id>/', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]
