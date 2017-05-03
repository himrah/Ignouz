from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *
class Abc(SummernoteModelAdmin):
 #   admin.site.register(QOA)
    admin.site.register(Subject)
    admin.site.register(Question)
    admin.site.register(Comment)
    admin.site.register(Sessions)
    admin.site.register(Years)
admin.site.register(QOA,Abc)
admin.site.register(Answer,Abc)
# Register your models here.
