from django.shortcuts import render, redirect
from .models import * 
from django.contrib import messages

def index(request): 
    orderedQuestion = Question.objects.order_by('-created_at')
    listOfQuestion = []
    index = 0 
    while index < len(orderedQuestion) and index < 5 :
        listOfQuestion.append(orderedQuestion[index])
        index = index + 1 
    content ={
        'questions' : listOfQuestion,
        'user' : User.objects.get(id=request.session['user']),
        'comments' : Comment.objects.all(),
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
    orderedQuestion = Question.objects.order_by('-created_at')
    content ={
        'questions' : orderedQuestion,
        'user' : User.objects.get(id=request.session['user']),

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
        )
    return redirect('/displayQuestion')

####################### End Question part ########################
def displayAnswerFrom(request, question_id):
    content = {
        'question' : Question.objects.get(id= question_id),
        'comments' : Comment.objects.all(),
        'user' : User.objects.get(id= request.session['user']),
    }
    return render(request, 'displayAnswerFrom.html', content)

def addAnswer(request, question_id):
    print(question_id)
    if request.method == "POST":
        Comment.objects.create(
            comment_text= request.POST['comment_text'],
            user = User.objects.get(id = request.session['user']),
            question = Question.objects.get(id = question_id)
        )
        return redirect('/displayAnswerFrom/'+str(question_id))

##################### End Answer process and display ############### 
################### modifiy Edit and Delete ########################

def delete(request, comment_id, question_id): 
        dell = Comment.objects.get(id=comment_id)
        dell.delete()
        return redirect('/displayAnswerFrom/'+str(question_id))

def displayEdit(request, comment_id): 
    content = {
        'comments' : Comment.objects.get(id=comment_id)
    }
    return render(request, 'displayEdit.html')
