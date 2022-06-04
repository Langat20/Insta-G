from django.db import models
from accounts.models import UserAccount
from cloudinary.models import CloudinaryField

class Post(models.Model):
    host = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True)
    image = CloudinaryField("image")
    description = models.CharField(max_length=100)
    liked = models.ManyToManyField(UserAccount, blank=True, null=True, related_name='liked')
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description


