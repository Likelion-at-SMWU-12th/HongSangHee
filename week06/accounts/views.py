from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from users.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view

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

@api_view(['POST'])
def signup_api(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    password2 = request.data.get('password2')
    #비밀번호 유효성 검사
    if password != password2:
        return Response({"message": "비밀번호를 다시 확인하세요"})

    # 회원가입 시도하기
    try:
        user = User.objects.create_user(username=username, email=email, password=password)
        return Response({"회원가입 성공"})
    
    except : 
        return Response({"회원가입 실패"})


@api_view(['POST'])
def login_api(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username = username, password = password)

    if user is not None : #로그인 실패(user 객체 반환 실패)
        return Response({"message": "로그인 성공", "data":request.data})
    
    else : 
        return Response({"로그인 정보를 다시 확인하세요"})