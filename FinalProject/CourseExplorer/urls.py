from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('index/', views.user_index, name='index'),
    path('search/', views.user_search, name='search'),
    path('landing/', views.landing,name = 'search')
]
