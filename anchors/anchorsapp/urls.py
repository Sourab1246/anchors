from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('top-earning-videos/', views.top_earning_videos, name='top_earning_videos'),
    path('user-profile/', views.user_profile, name='user_profile'),
    path('upload-video/', views.upload_video, name='upload_video'),
    path('notifications/', views.notifications, name='notifications'),
    path('settings/', views.settings, name='settings'),
    path('logout/', views.logout_view, name='logout'),
    path('upload/', views.upload_video, name='upload_video'),
    
]