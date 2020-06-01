from django.db import models
from django.utils import timezone


class MiniURL(models.Model):
    url = models.URLField(unique=True)
    code = models.CharField(max_length=32, unique=True)
    date = models.DateTimeField(default=timezone.now())
    author = models.CharField(max_length=32)
    redirect_access = models.IntegerField(default=0)

    def __str__(self):
        return self.code

    class Meta:
        ordering = ['date']
