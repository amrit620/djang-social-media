from django.urls import path,include 
from . import views


urlpatterns = [
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.register,name="register"),
    path('',views.home,name="home"),
    path('create_post/',views.createPost,name="create")
]