from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class UserDetail(models.Model):
    user_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name


class BookingDetail(models.Model):
    user = models.ForeignKey(UserDetail,on_delete=models.CASCADE)
    adult = models.IntegerField()
    minor = models.IntegerField()
    infant = models.IntegerField()
    total_price = models.IntegerField()

    def __unicode__(self):
        return self.minor


class BookingPrice(models.Model):
    adult_price = models.IntegerField()
    minor_price = models.IntegerField()
    infant_price = models.IntegerField()

    def __unicode__(self):
        return self.adult_price



