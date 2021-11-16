"""user URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView,PasswordResetDoneView,PasswordResetCompleteView,PasswordResetConfirmView
from django.conf.urls import url
from django.conf import settings



urlpatterns = [
    path('', views.home, name="home"),
    path('logout/', LogoutView.as_view(), {'/': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('password/password_reset_sent/', PasswordResetDoneView.as_view(template_name='password/password_reset_sent.html'), name='password_reset_sent'),
    path('password_reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="password/password_reset_new_password.html"), name='password_reset_new_password'),
    path('reset_done/', PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),
]
