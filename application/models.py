from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
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

class QOA(models.Model):
    question = models.TextField()
    ans = models.TextField()
    year = models.IntegerField()
    session = models.CharField(max_length=10)
    def __str__(self):
        return  self.question

class Subject(models.Model):
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=30)
    QandA = models.ForeignKey(QOA,on_delete=models.CASCADE)
    def __str__(self):
        return self.code



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
    ans = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
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

