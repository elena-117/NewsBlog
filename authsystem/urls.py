from django.urls import path
from . import views

urlpatterns = [

    # path('', views, name="join"),

    path('my-login', views.my_login, name="my-login"),

    path('register', views.register, name="register"),

    path('dashboard', views.dashboard, name="dashboard"),

    path('user-logout', views.user_logout, name='user-logout')

] 

