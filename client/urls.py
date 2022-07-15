from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'client', views.ClientList)

app_name="main"
urlpatterns = [
    # path('', views.addClient,name="loginform"),
    path('api/', include(router.urls)),
    path('', views.getclientinfo, name="client"),

]
