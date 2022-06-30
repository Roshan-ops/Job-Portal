from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm, PasswordInput, TextInput

from account.managers import CustomUserManager

JOB_TYPE = (
    ('M', "Male"),
    ('F', "Female"),

)
JOB_LEVEL =(
    ('B', "Beginner"),
    ('I', "Intermidiate"),
    ('E', "Expert")

)


ROLE = (
    ('employer', "Employer"),
    ('employee', "Employee"),
)

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })
    role = models.CharField(choices=ROLE,  max_length=10)
    gender = models.CharField(choices=JOB_TYPE,  max_length=1)
    gender = models.CharField(choices=JOB_LEVEL, max_length=1)
    level =  models.CharField(choices=JOB_TYPE, max_length=1)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name+ ' ' + self.last_name
    objects = CustomUserManager()




   