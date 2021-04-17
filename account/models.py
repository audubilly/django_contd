from django.db import models


# Create your models here.

class Owner(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=15)
    bio = models.TextField(null=True)
    profile_picture = models.ImageField(default='user.png', upload_to='user_images')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
