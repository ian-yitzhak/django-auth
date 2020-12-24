from django.urls import path

from . import views

from django.contrib.auth import views as authview

urlpatterns = [
    path('registaration/', views.registration , name= "Register" ),

    path('', views.home , name= "home" ),


    path('login/', authview.LoginView.as_view(template_name= "login.html") ),


     path('logout/', authview.LogoutView.as_view(template_name= "logout.html") ),

   
]