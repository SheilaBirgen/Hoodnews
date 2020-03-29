from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Neighbourhood, Profile,Business

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


class NeighbourhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighbourhood
        fields = ('name', 'location','created_by', 'police', 'health_dpt','health_dpt_address', 'police_dpt_address' )
    


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'name', 'status', 'prof_pic', 'location', 'neighbourhood')

class BusinessSerializer(serializers.ModelSerializer):
    bsn__name = serializers.CharField()
    User = serializers.CharField()
    bsn_email = serializers.CharField()
   
    class Meta:
        model = Business
        exclude = ['is_active', 'neighborhood', 'id', 'owner']
