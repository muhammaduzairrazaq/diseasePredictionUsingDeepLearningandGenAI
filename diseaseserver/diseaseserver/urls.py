"""
URL configuration for diseaseserver project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
# from django.conf.urls import url
from chatbot.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ReactView.as_view(), name='chatbotview'),
    path('adax/signup/', UserRegistrationView.as_view(), name='signup'),
    path('adax/signin/', UserVerificationView.as_view(), name='signin'),
    path('adax/diseaseprofile/', DiseaseReportView.as_view(), name='profile'),
    path('adax/deletereport/', DeleteReportView.as_view(), name='deletereport'),
    path('adax/deleteaccount/', DeleteAccountView.as_view(), name='deleteaccount'),
]
