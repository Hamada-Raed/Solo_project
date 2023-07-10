from django.urls import path, include
from . import views

urlpatterns = [
    # display
    path('', views.index), 
    path('displayAboutUs', views.displayAboutUs), 
    path('success' ,views.success),
    path('failded', views.failded),
    #Log in and reigtration process
    path('signin', views.signin),
    path('register', views.register), 
    path('login', views.login), 
    #add question process
    path('displayAllQuestion', views.displayAllQuestion),
    path('displayFormQuestion', views.displayFormQuestion),
    path('addQuestion', views.addQuestion),
    #add answer process
    path('displayAnswerFrom/<question_id>', views.displayAnswerFrom), 
    path('addAnswer/<question_id>', views.addAnswer),
    #modifiy ex edit and delete
    path('delete/<comment_id>/<question_id>', views.delete),
    path('edit/<comment_id>/<question_id>', views.displayEditForm), 
    path('editQuestion/<question_id>', views.editQuestion), 
    
    

]