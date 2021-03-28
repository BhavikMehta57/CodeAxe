from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from multiselectfield import MultiSelectField
import uuid
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone_number, password=None):
        if not email:
            raise ValueError("Users must have an email")
        if not phone_number:
            raise ValueError("Phone Number Needed")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, first_name, last_name, phone_number, password):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password,
            phone_number=phone_number,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=60,unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.IntegerField(unique=True)
    # location = gismodels.PointField()
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','phone_number']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True

Services = (
    ("Vehicle Servicing","Vehicle Servicing"),
    ("Vehicle Breakdown Support","Vehicle Breakdown Support"),
    ("Vehicle Parts Replacement","Vehicle Parts Replacement"),
    ("Vehicle Modification","Vehicle Modification"),
    ("Body Repair & Repainting","Body Repair & Repainting"),
)

class Shop(models.Model):
    shop_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shop_name = models.CharField(max_length=50)
    owner_name = models.CharField(max_length=50)
    shop_email = models.EmailField(max_length=60,unique=True)
    shop_contact = models.IntegerField(unique=True)
    owner_contact = models.IntegerField(unique=True)
    shop_locality = models.CharField(max_length=50)
    shop_district = models.CharField(max_length=50)
    shop_city = models.CharField(max_length=50)
    shop_pincode = models.IntegerField()
    vehicle_servicing_charge = models.IntegerField()
    vehicle_breakdown_Support_charge = models.IntegerField()
    vehicle_parts_Replacement_charge = models.IntegerField()
    vehicle_modification_charge = models.IntegerField()
    body_repair_and_repainting_charge = models.IntegerField()
    shop_image = models.ImageField()

    def __str__(self):
        return self.shop_name

class Booking(models.Model):
    booking_id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    hired_shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    services_required = MultiSelectField(choices=Services)
    time = models.DateTimeField(default=timezone.now)
