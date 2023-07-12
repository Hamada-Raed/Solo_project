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
    return redirect('/displayAllQuestion')

####################### End Question part ########################
def displayAnswerFrom(request, question_id):
    orderedComment = Comment.objects.order_by('-created_at')
    countComment = len(orderedComment)
    content = {
        'questions' : Question.objects.get(id= question_id),
        'comments' : orderedComment,
        'user' : User.objects.get(id= request.session['user']),
        'countComment' : countComment,
    }
    return render(request, 'displayAnswerFrom.html', content)

def addAnswer(request, question_id):
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

def displayEditComment(request, comment_id, question_id): 
    content = {
        'user' : User.objects.get(id=request.session['user']),
        'comments' : Comment.objects.get(id=comment_id),
        'questions' : Question.objects.get(id=question_id),
    }
    return render(request, 'EditCommet.html', content)

def editComment(request, comment_id, question_id): 
    selected = Comment.objects.get(id=comment_id)
    selected.comment_text = request.POST['comment_text']
    selected.save()
    return redirect('/displayAnswerFrom/'+str(question_id))

def deleteQuestion(request, question_id):
    dell = Question.objects.get(id=question_id)
    dell.delete()
    return redirect('/displayAllQuestion')

def displayEditFromQuestion(request, question_id): 
    content = {
        'user' : User.objects.get(id=request.session['user']),
        'questions' : Question.objects.get(id=question_id),
    }
    return render(request, 'displayEditFromQuestion.html', content)

def editQuestion(request, question_id): 
    selected = Question.objects.get(id= question_id)
    selected.message_text = request.POST['message_text']
    selected.desc = request.POST['desc']
    selected.save()
    return redirect('/displayAllQuestion')

################This is a port of code to post message ############ 

def displayUsers(request): 
    numberOfUsers = len(User.objects.all())
    content = {
        'users' : User.objects.all(),
        'user' : User.objects.get(id=request.session['user']), 
        'count' : numberOfUsers
    }
    return render(request, 'displayUsers.html', content)

def distroy(request): 
    del request.session['user'] 
    del request.session['username']
    return('/')