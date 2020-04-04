from django.contrib import admin
from .models import Neighbourhood, Profile,Business,User,Department

# Register your models here.
admin.site.register(Neighbourhood)
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(User)
admin.site.register(Department)