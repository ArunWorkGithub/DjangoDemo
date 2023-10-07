"""
URL configuration for django_demo_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import django_demo_app.view as drink_view
from django_demo_myapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('hello/', views.hello),
    path('admin/', admin.site.urls),
    path('drinks/', drink_view.get_drinks_list),
    path('drink', drink_view.insert_drink),
    path('drinks/<int:id>', drink_view.drink_detail),
] 

urlpatterns = format_suffix_patterns(urlpatterns)