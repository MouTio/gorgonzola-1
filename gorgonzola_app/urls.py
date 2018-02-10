from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('subscription', views.subscription, name='about'),
]