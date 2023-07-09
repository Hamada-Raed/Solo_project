from django.shortcuts import render

def index(request): 
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')
    
def QandA(request): 
    return render(request, 'QandA.html' )

def all_subject(request): 
    return render(request, 'courses.html')

def signin(request): 
    return render(request, 'logregister.html')
