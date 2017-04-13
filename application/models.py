from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
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

class Subject(models.Model):
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=30)
    QandA = models.ForeignKey(QOA,on_delete=models.CASCADE)



class Answer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ans = models.TextField()
    date = models.DateTimeField()
    is_deleted = models.BooleanField(default=False)

class Question(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    is_delete = models.BooleanField(default=False)
    ans = models.ForeignKey(Answer,on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    forwhat = models.ForeignKey(Question,on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField()
    is_deleted = models.BooleanField(default=False)
