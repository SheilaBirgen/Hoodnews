from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
import datetime as dt


# Create Profile when creating a User
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

    NeighbourhoodAdmin.objects.create(user=instance)


class Neighbourhood(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64, null=True)
    created_by =  models.CharField(max_length=64, null=True)
    police = models.CharField(max_length=20)
    health_dpt = models.CharField(max_length=20)
    health_dpt_address = models.CharField(max_length=20)
    police_dpt_address = models.CharField(max_length=20)

    def __str__(self):
        return f' {self.name} Community'


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
    Neighbourhood_id = models.ForeignKey(User,on_delete=models.CASCADE)
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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    user_name = models.CharField(max_length=30,blank=True)
    prof_pic = models.ImageField(upload_to= 'profiles/', blank=True,default="profile/a.jpg")
    bio = models.CharField(max_length=800,default="Welcome Me!")

    def __str__(self):
        return f'{self.user.username} User'
