from django.urls import path, include
from . import views
from .views import *
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
   path('api/auth/', obtain_auth_token),
   path('api/hood/', views.NeighbourhoodList.as_view()),
   path("login/", LoginView.as_view(), name="login"),
   path('api/v1/profile/<int:pk>/<int:id>', views.ProfileList.as_view()),
   path('api/v1/create_business/<int:pk>', views.CreateBusinessView.as_view()),
   path('api/v1/post', views.CreatePostView.as_view()),
   path('api/v1/create_business/<int:pk>', views.CreateDepartmentView.as_view()),
   path('admin/<int:id>/edit_hood_info/<int:pk>/', EditHoodInfo.as_view(), name="edit_hood_info"),
   path('admin/<int:id>/delete_hood/<int:pk>/', DeleteHood.as_view(), name="delete_hood"),
]