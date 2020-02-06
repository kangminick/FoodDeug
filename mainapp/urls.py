from django.urls import path
from . import views
urlpatterns = [
    path('', views.main, name='main'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('swipe/', views.swipe, name='swipe'),
    path('mypage/', views.mypage, name='mypage'),
    path('detail/<int:r_code>', views.detail, name='detail'),
    path('like/', views.like, name='like'),
    path('about/', views.about, name='about'),
    path('recognition/', views.recognition, name='recognition'),
]