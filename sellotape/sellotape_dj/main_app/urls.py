from django.urls import path

from . import views

urlpatterns = [
    path('complete-login/', views.complete_login, name='complete-login'),
    path('', views.landing, name='landing'),
    path('add-stream/', views.add_stream, name='add_stream'),
    path('follow/<str:username>/', views.follow, name='follow'),
    path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
    path('explore/', views.explore, name='explore'),
    path('trending/', views.trending, name='trending'),
    path('<str:username>/', views.user, name='user'),
]
