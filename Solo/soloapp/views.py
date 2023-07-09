from django.shortcuts import render, redirect
from .models import * 
from django.contrib import messages
def index(request): 
    content = {
        'users' : request.session['username']
    }
    return render(request, 'index.html', content )

def aboutus(request):
    return render(request, 'aboutus.html')
    
def QandA(request): 
    content = {
        'questions' : Message.objects.all().order_by('-created_at').values(),
        'users' : request.session['username'],
    }
    return render(request, 'QandA.html',content )

def all_subject(request): 
    return render(request, 'courses.html')

def signin(request): 
    return render(request, 'logregister.html')

def success(request):
    content = {
        'users' : request.session['username']
    }
    return render(request, 'success.html', content)

def failded(request):
    return render(request, 'failded.html')

def addQuestion(request): 
    content = {
        'users' : request.session['username']
    }
    return render(request, 'addQuestion.html', content)

def register(request):
    errors = User.objects.regValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/failded')
    else:
        User.objects.create(
        username= request.POST['username'], 
        email=request.POST['email'], 
        password=request.POST['password'])
        return render(request, 'logregister.html')

def login(request):
    errors = User.objects.loginValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return render(request, 'logregister.html')
    else:
        user = User.objects.get(email = request.POST['email'])
        request.session['user'] = user.id
        request.session['username'] = user.username
        return redirect('/success')

def addQ(request):
    if request.method == 'POST':
        Message.objects.create(
            message_text = request.POST['message_text'],
            user = User.objects.get(id=request.session['user'])
        ).orderd_
    return redirect('/QandA')

def anwser(request, question_id):
    content = {
        'question' : Message.objects.get(id=question_id),
        'users' : request.session['username']
    }
    return render(request, 'answer.html', content)

