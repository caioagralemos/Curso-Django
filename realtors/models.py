from django.db import models
from datetime import datetime

# Create your models here.

class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now(), blank= True)
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.photo.url.startswith('/curso_django/media/photos/'):
            x = self.photo.url.replace('/curso_django/media/', '')
            self.photo.url = f' /www/media/curso_django/{x}'
        super().save(*args, **kwargs)