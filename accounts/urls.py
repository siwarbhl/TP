from django import views
from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
from django.urls import include
import path
from django.conf.urls.static import static

from mysite import settings


urlpatterns = [
path('login/', views.LoginView.as_view(), name='login'),
path('logout/', views.LogoutView.as_view(), name='logout'),
path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]