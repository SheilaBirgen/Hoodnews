from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import NeighbourhoodSerializer, ProfileSerializer, UserSerializer, BusinessSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsAdminOrReadOnly
from django.contrib.auth import login, logout
from .models import *
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated

# @csrf_exempt
# def get_data(request):
# 	data = ExampleModel.objects.all()
# 	if request.method == 'GET':
# 		serializer = ExampleModelSerializer(data, many=True)
# 		return JsonResponse(serializer.data, safe=False)



class UserCreate(APIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request, ):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileList(APIView):
    def get_queryset(self):
        queryset = Profile.objects.filter(user_id=self.kwargs["pk"])
        return queryset

    serializer_class = ProfileSerializer

    def put(self, request, *args, **kwargs):
        profile = Profile.objects.get(pk=self.kwargs["pk"])
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
    def get_hood(self, pk):
        try:
            return Neighbourhood.objects.get(pk=pk)
        except Neighbourhood.DoesNotExist:
            return Http404
    def get(self,request,pk, format=None):
        businesses = Business.objects.filter(neighbourhood_id=pk)
        serializers = BusinessSerializer(businesses, many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
       
    def post(self, request, pk, format=None):
        hood = self.get_hood(pk)
        serializers = BusinessSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save(user=request.user,neighbourhood=hood)
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
    def get_hood(self, pk):
        try:
            return Neighbourhood.objects.get(pk=pk)
        except Neighbourhood.DoesNotExist:
            return Http404
    def get(self,request,pk, format=None):
        department = Department.objects.filter(neighbourhood_id=pk)
        serializers = DepartmentSerializer(department, many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    
    def post(self,request,pk,format=None):
        hood = self.get_hood(pk)
        serializers = DepartmentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save(neighbourhood=hood)
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteHood(generics.DestroyAPIView):
    def destroy(self, request, *args, **kwargs):
        system_admin = SystemAdmin.objects.get(pk=self.kwargs["id"])
        if system_admin.is_admin:
            try:
                queryset = Neighbourhood.objects.get(pk=self.kwargs["pk"])
            except ObjectDoesNotExist:
                return Response({"Neighbourhood does not exist"}, status=status.HTTP_400_BAD_REQUEST)

            queryset.delete()
            return Response({"Neighbourhood deleted"})

        else:
            return Response({"Not authorized"}, status=status.HTTP_400_BAD_REQUEST)