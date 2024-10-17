"""collegewebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from collegeapp import views
from collegeapp import navview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',navview.login),
    path('validation/',navview.validation),
    path('exit/',navview.login),
    
    path('ahome/',navview.adminhome),
    path('aaddprofile/',navview.admin_addprofile),
    path('adues/',navview.admin_dues),
    path('anotification/',navview.admin_notification),
    path('afeedback/',navview.admin_feedback),
    path('aviewprofile/',navview.admin_view),
    path('reg/',views.registration),
    path('dueform/',views.duesform),
    path('duedetail/',views.viewduedetails),
    path('updatedue/',views.updatedue),
    path('send/',views.notificateon),
    #parent path
 path('phome/',navview.parenthome),
 path('childdue/',views.parentdue),
 path('parentnot/',views.parentnotification),
 path('parentfeed/',views.parentfeedback),
 path('mapdue/',views.mapdue),
 #student path
 path('shome/',navview.studenthome),
 path('scd/',navview.studentdues),
 path('sfeedback/',navview.studentfeedbacks),
 path('noti/',navview.studentnotification),
 path('ssm/',navview.studentstudymaterial),
 path('sr/',navview.studentresult),
 path('smapd/',views.stmapdue),
 path('stfeed/',views.sendfeed),
 path('upc/',views.uploadcours),
 path('dc/',views.deletecourse),
 path('lk/',views.courseview),
 path('playv/<int:id>/', views.linkdata, name='play_video'),
path('fpv/',navview.forgetpass),
path('validationpassword/',navview.passwordcheck),
path('del/<int:contactno>/',views.deletfeed,name='del'),
   
]
