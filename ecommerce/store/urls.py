from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.loginpage, name="loginpage"),
    path('logout/', views.logoutpage, name="logout"),
    path('forgetpassword/', views.forgetpassword, name = "forgetpassword"),
    path('otpscreen', views.otpscreen , name='otpscreen'),
    path('resetpassword/<str:email>/', views.resetpassword, name= 'resetpassword'),
]
