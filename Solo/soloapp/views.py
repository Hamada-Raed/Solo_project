from django.shortcuts import render

def index(request): 
    return render(request, 'index.html')

def QandA(request): 
    return render(request, 'QandA.html' )

def all_subject(request): 
    return render(request, 'courses.html')
