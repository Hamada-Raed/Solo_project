from django.shortcuts import render, redirect
from .models import * 
from django.contrib import messages

def index(request): 
    content = {
        'user' : User.objects.get(id= request.session['user'])
    }
    
    return render(request, 'index.html', content )

def displayAboutUs(request):
    return render(request, 'aboutus.html')

#######################  Log in and registerion process and pages ##############
def signin(request): 
    return render(request, 'logregister.html')

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

def success(request):
    content = {
        'user' : request.session['username']
    }
    return render(request, 'success.html', content)

def failded(request):
    return render(request, 'failded.html')

######################### End LOGIN registration part ###########
######################### Add Question process and display ######
def displayAllQuestion(request): 
    content ={
        'questions' : Question.objects.all().order_by('-created_at'),
        'user' : User.objects.get(id=request.session['user'])
    }
    return render(request, 'displayAllQuestion.html', content)

def displayFormQuestion(request): 
    content = {
        'user' : User.objects.get(id=request.session['user'])
    }
    return render(request, 'addQuestion.html', content)
    
def addQuestion(request):
    if request.method == 'POST':
        Question.objects.create(
            message_text = request.POST['message_text'],
            desc = request.POST['desc'],
            user = User.objects.get(id=request.session['user'])
        ).orderd_by('created_at')
    return redirect('/displayQuestion')

####################### End Question part ########################
def displayAnswerFrom(request, question_id):
    content = {
        'question' : Question.objects.get(id= question_id),
        'comments' : Comment.objects.all(),
        'user' : User.objects.get(id= request.session['user']),
        'request' : request
        
    }
    return render(request, 'displayAnswerFrom.html', content)

def addAnswer(request, question_id):
   if request.method == "POST":
        Comment.objects.create(
            comment_text= request.POST['comment_text'],
            user = User.objects.get(id = request.session['user']),
            question = Question.objects.get(id = question_id))

        return redirect('/addAnswer/'+str(question_id))

##################### End Answer process and display ############### 
################### modifiy Edit and Delete ########################

def modifiy(request, comment_id): 
    if 

