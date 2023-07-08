from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('QandA', views.QandA),
    path('all_subject', views.all_subject)
]