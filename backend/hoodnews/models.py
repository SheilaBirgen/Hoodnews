from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
import datetime as dt

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    user_name = models.CharField(max_length=30,blank=True)
    prof_pic = models.ImageField(upload_to= 'profiles/', blank=True,default="profile/a.jpg")
    bio = models.CharField(max_length=800,default="Welcome Me!")

    def post(self, form):
        image = form.save(commit=False)
        image.user = self
        image.save()


class Neighbourhood(models.Model):
    name = models.CharField(max_length = 65)
    location  = models.CharField(max_length=65)
    occupants = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Location'

    @classmethod
    def search_hood(cls, search_term):
        hoods = cls.objects.filter(name__icontains=search_term)
        return hoods


    def __str__(self):
        return f"{self.location}"


    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()
class Post(models.Model):
    title = models.CharField(max_length = 65)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighbourhood, blank=True)
    description = models.TextField(max_length=300)
    
    
        
    def __str__(self):
        return self.description


class Business(models.Model):
    name = models.CharField(max_length = 65)
    user = models.ForeignKey(User)
    hood = models.ForeignKey(Neighbourhood,blank=True)
    email = models.CharField(max_length=100)


    def __str__(self):
        return self.name


    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

class Join(models.Model):
    user_id = models.OneToOneField(User)
    hood_id = models.ForeignKey(Neighbourhood)

    def __str__(self):
        return self.user_id
