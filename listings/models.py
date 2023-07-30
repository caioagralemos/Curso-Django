from django.db import models
from datetime import datetime
from realtors.models import Realtor

# Create your models here.

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=None)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now())
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.photo_main:
            x = self.photo_main.url.replace('/curso_django/media/', '')
            self.photo_main.url = f' /www/media/curso_django/{x}'
        if self.photo_1:
            x = self.photo_1.url.replace('/curso_django/media/', '')
            self.photo_1.url = f' /www/media/curso_django/{x}'
        if self.photo_2:
            x = self.photo_2.url.replace('/curso_django/media/', '')
            self.photo_2.url = f' /www/media/curso_django/{x}'
        if self.photo_main:
            x = self.photo_3.url.replace('/curso_django/media/', '')
            self.photo_3.url = f' /www/media/curso_django/{x}'
        if self.photo_main:
            x = self.photo_4.url.replace('/curso_django/media/', '')
            self.photo_4.url = f' /www/media/curso_django/{x}'
        if self.photo_main:
            x = self.photo_5.url.replace('/curso_django/media/', '')
            self.photo_5.url = f' /www/media/curso_django/{x}'
        if self.photo_main:
            x = self.photo_6.url.replace('/curso_django/media/', '')
            self.photo_6.url = f' /www/media/curso_django/{x}'
        super().save(*args, **kwargs)