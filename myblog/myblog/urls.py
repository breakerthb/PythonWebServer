"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

from user_manage import views as usr_m_views

urlpatterns = [
    url(r'^$', usr_m_views.index, name = 'index'),
    url(r'^home', usr_m_views.index, name = 'home'),
    url(r'^userlist', usr_m_views.userlist, name = 'userlist'),
    url(r'^useradd', usr_m_views.useradd, name = 'useradd'),
    url(r'^userdel', usr_m_views.userdel, name = 'userdel'),
    url(r'^usersearch', usr_m_views.usersearch, name = 'usersearch'),
    url(r'^searchret', usr_m_views.searchret, name = 'searchret'),
    url(r'^admin/', admin.site.urls),
]
