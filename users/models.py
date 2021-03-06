from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    picture = models.ImageField('Foto de perfil', default='img/blank-pic.png')
    following = models.ManyToManyField('self', related_name='following_users', blank=True, symmetrical=False)
    followers = models.ManyToManyField('self', blank=True, symmetrical=False)

    @property
    def following_count(self):
        return self.following.count()
    
    @property
    def followers_count(self):
        return self.followers.count()
