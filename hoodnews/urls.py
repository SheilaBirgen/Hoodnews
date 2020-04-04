from django.urls import path, include
from . import views
from .views import *
from rest_framework_simplejwt import views as jwt_views
from django.contrib.auth import views as auth_views
from rest_framework import routers

urlpatterns = [
   path('api/hood/', views.NeighbourhoodList.as_view()),
   path('api/user', views.UserList.as_view()),
   path('register/', RegisterUser.as_view(), name='register'),
   path('api/v1/profile/<int:pk>/<int:id>', views.EditProfileView.as_view()),
   path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/v1/create_business/', views.CreateBusinessView.as_view()),
   path('api/v1/post', views.CreatePostView.as_view()),
   path('api/v1/create_dept/', views.CreateDepartmentView.as_view()),
  
]