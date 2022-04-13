
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, email, password_1 = None, password_2 = None):
        if not email:
            return ValueError('User must have an email address')
        if not username:
            return ValueError('User must have a username')

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email = self.normalize_email(email),
        )

        if password_1 == password_2:
            user.set_password(password_1)
            user.save(using = self._db)

        return user

    def create_superuser(self, username, first_name, last_name, email, password_1, password_2):
        user = self.model(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = self.normalize_email(email)
        )
        if password_1 == password_2:
            user.set_password(password_1)

        user.is_admin = True
        
class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length= 200)
    last_name = models.CharField(max_length= 200)
    email = models.EmailField(max_length= 200, unique=True)
    password_1 = models.CharField(max_length=100)
    password_2 = models.CharField(max_length= 100)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    phone = models.IntegerField(blank=False)
    isVerified = models.BooleanField(blank=False, default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'email', 'password', ]

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


#: for OTP Verification
class phoneModel(models.Model):
    Mobile = models.IntegerField(blank=False)
    isVerified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0, blank=False)

    def __str__(self):
            return str(self.Mobile)
