from django.urls import path, include
from . import views

urlpatterns = [
    # display pages
    path('', views.index),
    path('aboutus', views.aboutus),
    path('QandA', views.QandA),
    path('all_subject', views.all_subject),
    path('signin', views.signin),
    path('success' ,views.success),
    path('failded', views.failded),
    path('addQuestion', views.addQuestion),

    #functions 
    path('register', views.register),
    path('login', views.login),
    path('addQ', views.addQ),
    path('anwser/<question_id>', views.anwser),
    # path('addAnswer', views.addAnswer),

]