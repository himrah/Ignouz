"""ignouz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django_summernote import urls as u
from application.views import *
from ckeditor_uploader import urls
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^ckeditor/', include(urls)),
    url(r'^summernote/',include(u)),
    url(r'^admin/', admin.site.urls),
    url(r'^$',index,name='Index'),
    url(r'^accounts/login/$',login,name='login'),
    url(r'^auth/$',auth_view,name='auth'),
    url(r'^accounts/logout/$',logout,name='logout'),
    url(r'^grade',grade,name='grade'),
    url(r'^community/comment/(?P<pk>\d+)',post_comment,name='post_comment'),
    url(r'^community/answer/(?P<pk>\d+)', ajax_answer, name='ajax_answer'),
    url(r'^result',result,name='result'),
    url(r'^accounts/registration/$',registration,name='registration'),
    url(r'^community/(?P<pk>.*)/', anss, name='answer'),
    url(r'^community/',community,name='community'),
    url(r'^answer/',answer,name='community'),
    url(r'^question_paper/$',question,name='question'),
    url(r'^question_paper/(?P<year>\d+)/(?P<month>\d+)/(?P<code>\d+)/$', question_paper, name='ques'),
    url(r'^question_paper/(?P<year>\d+)/(?P<month>\d+)/$',code_list,name='code_list'),

#    url(r'^question_paper/(?P<year>\d+)/(?P<month>\d+)/(?P<code>\d+)/$',question_paper, name='code_list'),
    url(r'^em',em,name='em'),
    #url('^test/',TemplateView.as_view(template_name='test.html'))
    url(r'^test/(?P<pk>.*)/',test,name='test')
]
