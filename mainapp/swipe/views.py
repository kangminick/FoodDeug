from django.shortcuts import render
from django.http import HttpResponse


def swipe(request): #스와이프 화면
    return render(
    request,
    'mainapp/swipe.html',
    {})

def like(request): #좋아요 리스트 화면
    return render(request, 'mainapp/like.html', {})

def mypage(request): #마이페이지
    return render(request,
    'mainapp/mypage.html',
    {})

def about(request): #어바웃 페이지
    return render(request, 'mainapp/about.html', {})

def detail(request, r_code): #음식점 상세페이지 O
    return render(request, 'mainapp/detail/%s.html' % r_code,{})
    #후에 return render(request, 'mainapp/detail.html',{mysite의 detail.html 참고})
#모델에 food_id 존재후 작성가능