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
from django.conf.urls import url
from django.contrib import admin
from application.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index,name='Index'),
    url(r'^accounts/login/$',login,name='login'),
    url(r'^auth/$',auth_view,name='auth'),
    url(r'^accounts/logout/$',logout,name='logout'),
    url(r'^grade',grade,name='grade'),
    url(r'^result',result,name='result'),
    url(r'^accounts/registration/$',registration,name='registration'),
    url(r'^answer/(?P<pk>.*)/', anss, name='answer'),
    url(r'^community/',community,name='community'),

    url(r'^em',em,name='em')

]
