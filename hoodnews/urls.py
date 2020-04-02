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
   path('api/user', views.UserList.as_view()),
   path('api/v1/profile/<int:pk>/<int:id>', views.EditProfileView.as_view()),
   # path("login/", LoginView.as_view(), name="login"),
   path('api/v1/create_business/<int:pk>', views.CreateBusinessView.as_view()),
   path('api/v1/post', views.CreatePostView.as_view()),
   path('api/v1/create_dept/<int:pk>', views.CreateDepartmentView.as_view()),
  
]