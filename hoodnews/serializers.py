from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Neighbourhood, Profile,Business,User,Department

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def validate_password(self, value: str) -> str:
        return make_password(value)


class NeighbourhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighbourhood
        fields = ('name', 'location','created_by' ,'occupants' )
    


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'name', 'status', 'prof_pic', 'location', 'neighbourhood')

class BusinessSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Business
        fields = ['bsn_name', 'bsn_email']
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['police', 'health_dpt', 'health_dpt_address', 'police_dpt_address', 'neighbourhood']