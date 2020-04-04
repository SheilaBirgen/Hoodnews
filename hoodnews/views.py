from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import NeighbourhoodSerializer, ProfileSerializer, UserSerializer, BusinessSerializer,DepartmentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsAdminOrReadOnly
from django.contrib.auth import login, logout
from .models import *
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import status


class RegisterUser(APIView):
    permission_classes = ()

    def post(self, request, ):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class UserList(APIView):
    def get(self, request, format=None):
        all_users = User.objects.all()
        serializers = UserSerializer(all_users,many=True)
        return Response(serializers.data)
    def post(self, request,format=None):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class NeighbourhoodList(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, format=None):
        hoods = Neighbourhood.objects.all()
        serializers = NeighbourhoodSerializer(hoods, many=True)
        return Response(serializers.data)


    def post(self, request, format=None):
        serializers = NeighbourhoodSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateBusinessView(APIView):
    permission_classes = (IsAuthenticated,)
    def get_business(self):
        try:
            return Business.objects.all()
        except Neighbourhood.DoesNotExist:
            return Http404
       
       # gets all businesses
    def get(self,request, format=None):
        biz = self.get_business()
        serializers = BusinessSerializer(biz, many=True)
        return Response(serializers.data)
       
    def post(self, request, format=None):
        serializers = BusinessSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class CreatePostView(APIView):
    permission_classes  = (IsAuthenticated,)

    def get(self,request, format=None):
        all_posts = Post.objects.all()
        serializers = PostSerializer(all_posts, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
            
            serializers.save(user=request.user)
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateDepartmentView(APIView):
    permission_classes = (IsAuthenticated,)
    def get_department(self):
        try:
            return Department.objects.all()
        except Neighbourhood.DoesNotExist:
            return Http404
        #gets all departments
    def get(self,request, format=None):
        dept = self.get_department()
        serializers = DepartmentSerializer(dept, many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
        serializers = DepartmentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class EditProfileView(APIView):
    permission_classes = (IsAuthenticated,)
    def get_profile(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404
    def get_hood(self, id):
        try:
            return Neighbourhood.objects.get(id=id)
        except Neighbourhood.DoesNotExist:
            return Http404
    def put(self, request,pk,id,format=None):
        profile = self.get_profile(pk)
        hood = self.get_hood(id)
        serializers = ProfileSerializer(profile,data=request.data)
        if serializers.is_valid():
            serializers.save(user=request.user, neighbourhood=hood)
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    