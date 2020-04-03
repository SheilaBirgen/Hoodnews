from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
import datetime as dt
from django.conf import settings


# Create Profile when creating a User
class Neighbourhood(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64, null=True)
    created_by =  models.CharField(max_length=64, null=True)
    police = models.CharField(max_length=20)
    health_dpt = models.CharField(max_length=20)
    health_dpt_address = models.CharField(max_length=20)
    police_dpt_address = models.CharField(max_length=20)
    occupants = models.IntegerField(default=0)
    
    def __str__(self):
        return f' {self.name} Community'
    def save_hood(self):
        self.save()
    def delete_hood(self):
        self.delete()

    def get_absolute_url(self):
        return reverse('profile')
    @classmethod
    def find_neigborhood(cls,search_term):
        search_result = cls.objects.filter(bsn_name__icontains=search_term)
        return search_result   
    @classmethod
    def create_neigborhood(cls):
        cls.save()
    @classmethod
    def delete_neigborhood(cls, id):
        delet = cls.objects.filter(id=id).delete()
                   
    @classmethod
    def update_occupants(cls,id):
        bsn = cls.objects.filter(id=id).update()
        return bsn 


class Business(models.Model):
    bsn_name = models.CharField(max_length=64, unique= True)
    Neighbourhood_id = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    User = models.ForeignKey(Neighbourhood, null=True, on_delete=models.CASCADE)
    bsn_email = models.EmailField(max_length=64, unique= True) 
    
    def get_absolute_url(self):
        return reverse('home')  

    @classmethod
    def search_by_bsn(cls,search_term):
        search_result = cls.objects.filter(bsn_name__icontains=search_term)
        return search_result   
    @classmethod
    def create_business(cls, **kwargs):
        loca = Neighbourhood.objects.get(id=request.user.profile.community.id)  
        new_business = Business(bsn_name=bizna,bsn_user=request.user,bsn_community=loca,bsn_email=email)
        new_business.save()
    @classmethod
    def delete_business(cls, id):
        delet = cls.objects.filter(id=id).delete()
                   
    @classmethod
    def update_business(cls,id):
        bsn = cls.objects.filter(id=id).update()
        return bsn 

class User(models.Model):
    name = models.TextField(max_length=50)
    Neighbourhood_id = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.EmailField(max_length=30)
    id = models.PositiveIntegerField(primary_key=True)
    status = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.user.username} User'

class Profile(models.Model):
    bio = models.TextField(max_length=50)
    Neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True)
    general_location = models.CharField(max_length=20, null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username} User'
        
    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()
    
    @classmethod
    def get_prof_id(cls, id):
        profile = cls.objects.get(pk=id)
        return profile
    def update_bio(self, bio):
        self.bio = bio
        self.save()
