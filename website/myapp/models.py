from django.db import models

class UserRegister(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    username = models.EmailField()
    mobile = models.BigIntegerField()
    password = models.CharField(max_length=20)
    confirmPassword = models.CharField(max_length=20)
    

class notesdata(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    file=models.FileField(upload_to='User_Notes')
    description=models.TextField()

class feedback(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    msg=models.TextField()




    