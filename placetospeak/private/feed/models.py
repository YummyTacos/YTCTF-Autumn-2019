from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    isPublic = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Friend(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='creator')
    following = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')

    def __str__(self):
        return f'{self.creator} - {self.following}'
