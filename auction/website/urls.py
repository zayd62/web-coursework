from django.urls import path, include
from website import views
urlpatterns = [
    # main page
    path('', views.index, name='index'),
    # signup page
    path('signup/', views.signup, name='signup'),
    # register new user
    path('register/', views.register, name='register'),
    # login page
    path('login/', views.login, name='login'),
    # logout page
    path('logout/', views.logout, name='logout'),
]
