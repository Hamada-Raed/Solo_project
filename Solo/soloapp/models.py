from django.db import models
import re 

class UserManager(models.Manager):
    def regValidator(self, postData):
        errors = {}
        #input validations
        if len(postData['username']) < 2:
            errors['username'] = "First Name should atleast be 2 charecters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if User.objects.filter(email=postData['email']).exists():
            errors['email'] = "This email is already registered!"
        if len(postData['password'] or postData['password_conf']) < 8:
            errors['password_len'] = "Password should atleast be 8 charecters"
        if postData['password'] != postData['password_conf']:
            errors['password_match'] = "Passwords do not match"
        return errors 

    def loginValidator(self, postData):
        errors = {}  
        if not (User.objects.filter(email=postData['email']) and User.objects.filter(password=postData['password'])):
            errors['login'] = "Login failed! Check email and password"

        return errors 

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager() 

class Question(models.Model):
    message_text = models.TextField()
    desc = models.TextField()
    user = models.ForeignKey(User, related_name='messages', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment_text = models.TextField()
    user = models.ForeignKey(User, related_name='comments', on_delete = models.CASCADE)
    question = models.ForeignKey(Question, related_name='comments', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
