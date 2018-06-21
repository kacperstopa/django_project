"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views

from recipes import views
from accounts import views as account_views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', account_views.signup, name='signup'),
    path('logout/', auth_views.logout, name='logout'),
    path('login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
    path('recipes/user/<username>', views.userrecipes, name='user_recipes'),
    path('recipes/<int:pk>', views.recipe, name='recipe'),
    path('recipes/<int:pk>/comments', views.comments, name='comments'),
    path('recipes/add', views.add, name='add'),
    path('recipes/delete/<int:pk>', views.delete, name='delete'),
    path('recipes/<int:pk>/comments/add', views.add_comment, name='add_comment'),
    path('admin/', admin.site.urls),
]
