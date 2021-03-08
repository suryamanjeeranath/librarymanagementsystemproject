"""Library_Managemen_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from booklib import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'Booklibrary/main',views.mainmenu),
    url(r'Booklibrary/addbook',views.addbook),
    url(r'Booklibrary/addstudent',views.addStudent),
    url(r'Booklibrary/issueh',views.issuebook),
    url(r'Booklibrary/studentlist',views.studentlist),
    url(r'Booklibrary/booklist',views.booklist),
    url(r'Booklibrary/issuedbooklist',views.issuedbooklist),
    #url(r'Booklibrary/studentissuedbooklist',views.studentissuedbooklist),
    url(r'Booklibrary/returnbook',views.returnbook),
    url(r'Booklibrary/returnbk', views.returnbk),
    #url(r'Booklibrary/pk', views.finecalculate),
    url(r'Booklibrary/issuedbookdelete', views.issuedbookdelete),
    #url(r'Booklibrary/finecal', views.finecal),
    #url(r'Booklibrary/finecalculate', views.finecalculate),
    url(r'Booklibrary/reg',views.reg),
    url(r'Booklibrary/login',views.login),
    url(r'Booklibrary/home', views.home),
    url(r'Booklibrary/searchbook', views.searchbook),
    url(r'Booklibrary/issuedbooksearch', views.issuedbooksearch),

]
