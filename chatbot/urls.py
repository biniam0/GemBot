from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, chatWithBot, chatHistory
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'),
         name='logout'),  # Redirect to the home page
    path('chat/', chatWithBot, name='chat'),
    path('history/', chatHistory, name='history'),


]
