from django.urls import path,include
from .views import quizapp, UserSignupView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('signup/',UserSignupView.as_view(template_name="quizApp/signup.html"), name="signup"),
    path('login/', LoginView.as_view(template_name="quizApp/login.html"), name="login"),
    path('', include('django.contrib.auth.urls')),
    path('', quizapp, name="quizapp"),
]