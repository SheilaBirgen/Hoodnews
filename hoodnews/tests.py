from django.test import TestCase
from .models import Neighbourhood,Profile,Business,User

# Create your tests here.
from django.contrib.auth.models import User


# Create your tests here.

class UserTestCase(TestCase):
    
    def setUp(self):
        self.super_admin = User(username="meg",email="meg@gmail.com",name="meg", role_type="SUPER ADMIN",is_superuser=True, is_staff=True, is_active=True)
        self.admin_user = User(username="june",email="hey@gmail.com",name="june", role_type="ADMIN",is_superuser=False, is_staff=True, is_active=True)
        self.user_one = User(username="danteh", email="test@gmail.com", name="dan", role_type="USER",is_superuser=False, is_staff=False, is_active=True)
        
    
    
    def test_save_superadmin(self):
        self.super_admin.save_sadmin()
        users = User.objects.all()
        self.assertTrue(len(users) > 0)
        
    def test_save_admin(self):
        self.admin_user.save_admin()
        users = User.objects.all()
        self.assertTrue(len(users)> 0)
    def test_save_user(self):
        self.user_one.save_user()
        users = User.objects.all()
        self.assertTrue(len(users) > 0)
        
class NeighbourhoodTestCase(TestCase):
    
    def setUp(self):
        self.admin_user = User(username="jack123",email="jack@gmail.com",name="Jack Doe", role_type="ADMIN",is_superuser=False, is_staff=True, is_active=True)
        self.hood_one = Neighbourhood(neighbourhood_name="Langata Estate", neighbourhood_location="Langata", occupants="100",admin_id=self.admin_user)
        
    
    def test_save_neighbourhood(self):
        self.admin_user.save_admin()
        self.hood_one.save_hood()
        hoods = Neighbourhood.objects.all()
        self.assertTrue(len(hoods)> 0)
        
    def test_delete_neighbourhood(self):
        self.admin_user.save_admin()
        self.hood_one.save_hood()
        self.hood_one.delete_hood()
        hoods = Neighbourhood.objects.all()
        self.assertTrue(len(hoods) == 0)
        
    def test_get_hoof_id(self):
        self.admin_user.save_admin()
        self.hood_one.save_hood()
        self.hood_one.get_hood_id(self.hood_one.id)
        hoods = Neighbourhood.objects.all()
        self.assertTrue(len(hoods) > 0)
        
    def test_update_hood_occupants(self):
        self.admin_user.save_admin()
        self.hood_one.save_hood()
        self.hood_one.get_hood_id(self.hood_one.id)
        self.hood_one.update_occupants("200")
        self.assertTrue(self.hood_one.occupants=="200")
        
class TestBusiness(TestCase):
    def setUp(self):
        self.user = User(username='rovin',
                         email='hey@gmail.com', password='moringa12')
        self.user.save()

        self.neighbourhood = Neigbourhood(
            name='southb', description='My neighbourhood', police_number=0, health_number=0)
        self.hood.save()

        self.busins = Business(name='Cyber', email='cyberfree@gmail.com',
                               description='all computer things', neighbourhood=self.hood, user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.busins, Business))

    def test_save_hood(self):
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)

    def test_delete_hood(self):
        business = Business.objects.all().delete()
        self.assertTrue(len(business) > 0)
