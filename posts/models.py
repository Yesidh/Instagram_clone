"""Post model"""

# Django
from django.db import models
from django.contrib.auth.models import User

# Local app
from users.models import Profile


class Post(models.Model):
    """Post model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """return post title and username"""
        return '{} by @{}'.format(self.title, self.user.username)
