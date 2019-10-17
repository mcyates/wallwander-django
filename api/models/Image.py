from django.db import models
from .User import User


class Image(models.Model):
    url = models.URLField()
    secure_url = models.URLField()
    title = models.CharField()
    height = models.CharField()
    width = models.CharField()
    imgFormat = models.CharField(verbose_name="format")
    nsfw = models.BooleanField(default="false")
    views = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    uploader = models.ForeignKey("User", on_delete=models.CASCADE)

