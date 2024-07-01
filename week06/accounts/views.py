from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

def signup_view(request):
    if request.method == 'GET':
        form = SignUpForm
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    
    else:
        form = SignUpForm(request.POST)

        if form.is_valid():
            instance = form.save()
            return redirect('index')
        else:
            return redirect('accounts:signup')
        
def login_view(request):
    # GET 요청 - 로그인 HTML 응답
    if request.method == "GET":
        return render(request, 'accounts/login.html', {'form': AuthenticationForm()})
    # POST 요청
    else:
        form = AuthenticationForm(request, request.POST) 
        if form.is_valid():
            login(request, form.user_cache)

            return redirect('index')
        else:
            return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):

    if request.user.is_authenticated:
        logout(request)
    return redirect('index')
