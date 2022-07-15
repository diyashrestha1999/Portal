from django.urls import path,include
from . import views
from django.contrib import admin
# from django.views.generic.base import TemplateView
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'client', views.ClientList)

app_name="main"
urlpatterns = [
    # path('', views.addClient,name="loginform"),
    # path('api/', include(router.urls)),
    path('',views.getclientinfo,name="client"),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
