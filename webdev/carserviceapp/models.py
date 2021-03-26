from django.db import models
<<<<<<< HEAD
=======
from django.contrib.auth.models import User
>>>>>>> eb5a199df0c3abc06b87d1a5c5613a81847c48eb
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
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