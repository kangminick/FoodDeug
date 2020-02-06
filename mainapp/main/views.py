from django.shortcuts import render
from django.http import HttpResponse

def main(request): #메인 화면
    return render(
    request, 
    'mainapp/index.html', 
    {})
def signin(request): #로그인 화면
    return render(
    request, 
    'mainapp/signin.html', 
    {})
def signup(request): #회원가입 화면
    return render(
    request, 
    'mainapp/signup.html', 
    {})