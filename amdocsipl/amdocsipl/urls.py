"""amdocsipl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from score_app import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('logout/', views.user_logout, name='logout'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('matches/', views.MatchDetailsView.as_view(), name='matches'),
    path('rules/', views.MatchRulesView.as_view(), name='rules'),
    path('players/', login_required(views.MatchPlayersView.as_view()), name='players'),
    path('wins/', login_required(views.MatchWinsView.as_view()), name='wins'),
    path('leaders/', login_required(views.MatchLeadersView.as_view()), name='leaders'),
]
