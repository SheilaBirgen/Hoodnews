from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, permissions
from .serializers import NeighbourhoodSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from django.contrib.auth import login, logout
from .models import *


# Create your views here.
class NeighbourhoodView(APIView):
    def get(self, request, format=None):
        hood = Neighbourhood.objects.all()
        serializer = ProjectSerializer(hood, many=True)
        return Response(serializer.data)

u
class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# Create your views here.
