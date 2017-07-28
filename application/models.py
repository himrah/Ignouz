from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
#from aloha.fields import HTMLField
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.



#class Profile(models.Model):
#    user = models.OneToOneField(User)
#    phone = models.IntegerField(null=True)
#    def __str__(self):
#        return "%User Profile" %self.user
    #id_deleted = models.BooleanField(default=False)
#@receiver(post_save, sender=User)
#def create_user_profile(sender,instance,created,**kwargs):
#    if created:
#        profile,created = Profile.objects.get_or_create(user=instance)

#post_save.connect(create_user_profile,sender=User)
        #Profile.objects.create(user=instance)
#@receiver(post_save,sender=User)ser has no prof
#def save_user_profile(sender,instance,created,**kwargs):
#    instance.profile.save()

class Sessions(models.Model):
    session = models.CharField(max_length=10)
    def __str__(self):
        return self.session

class Years(models.Model):
    year = models.IntegerField()
    def __str__(self):
        return str(self.year)


class Subject(models.Model):
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    time =models.CharField(max_length=20,blank=True)
    marks = models.CharField(max_length=20,blank=True)
    #QandA = models.ForeignKey(QOA,on_delete=models.CASCADE)
    def __str__(self):
        return self.code

class QOA(models.Model):
    q_no = models.CharField(max_length=10, blank=True)
    sub_q = models.CharField(max_length=3, blank=True)
    question = models.TextField()
    ans = models.TextField()
    course = models.CharField(max_length=3, blank=True)
    code = models.ForeignKey(Subject,on_delete=models.CASCADE)
    year = models.ForeignKey(Years,on_delete=models.CASCADE)
    session = models.ForeignKey(Sessions, on_delete=models.CASCADE)
    def __str__(self):
        return  self.question





class Question(models.Model):
    qs = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)
    is_delete = models.BooleanField(default=False)
    def __str__(self):
        return self.qs.replace(' ','-')
    #ans = models.ForeignKey(Answer,on_delete=models.CASCADE,null=True)


class Answer(models.Model):
    qes = models.ForeignKey(Question,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ans = RichTextField()
    date = models.DateTimeField(default=timezone.now(), blank=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return (str(self.qes)+" : "+str(self.ans))

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    forwhat = models.ForeignKey(Answer,on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.comment)+' ::::::::::::::: '+str(self.forwhat)

