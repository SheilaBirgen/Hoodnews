from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('profiles', views.ProfileView)


urlpatterns = [
    path('api_token_auth/', obtain_auth_token),
    path('profile_api/', include(router.urls)),
]