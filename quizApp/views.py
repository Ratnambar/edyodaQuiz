from django.shortcuts import render
from .models import Exam
from django.views.generic import CreateView
from .forms import SignUpForm
# Create your views here.



class UserSignupView(CreateView):
    template_name = "quizApp/signup.html"
    form_class = SignUpForm
    success_url = "/home"
    

# def profile_page_view(request):
#     user = request.user.id
#     # users = User.objects.get(id=user)
#     profiles = Profile.objects.get(user_id=user)
#     posts = Post.objects.filter(author=profiles)
#     print(profiles)
#     context = {
#         'profiles': profiles,
#         'posts': posts,
#     }
#     return render(request, 'quizApp/profile.html', context)




def quizapp(request):
    results = Exam.objects.all()
    return render(request,'quizApp/home.html',{"results":results})