from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class SignUpView(View):
    form_class = CustomUserCreationForm
    template_name = 'authenticate/Signup.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # or your home url name
        return render(request, self.template_name, {'form': form})

    


class SignInView(View):
    form_class = AuthenticationForm
    template_name = 'authenticate/Signin.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        return render(request, self.template_name, {'form': form})

        
class SignOutView(View): 
    def get(self, request):
        logout(request)
        return redirect('signin')


def home_view(request):
    return render(request, 'home.html')