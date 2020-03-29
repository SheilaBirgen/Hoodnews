from django.urls import path, include
from . import views
from .views import *
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


# router = routers.DefaultRouter()
# router.register('Neighbourhood', views.NeighbourhoodList)
# router.register('Profile', views.ProfileViewSet)


urlpatterns = [
   path('api/auth/', obtain_auth_token),
   # path(TemplateView.as_view(template_name="home.html"), name="home"),
   path('api/hood/', views.NeighbourhoodList.as_view()),
]