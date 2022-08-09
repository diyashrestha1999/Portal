from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'client', views.ClientList)

app_name="main"

from .api_view import DomainSuggestorAPIView
urlpatterns = [
    # path('', views.addClient,name="loginform"),
    path('api/', include(router.urls)),
    path('create/', views.ClientCreateViewSet.as_view({'post': 'create'}), name="create"),
    path('domain_availability/',DomainSuggestorAPIView.as_view())
]
