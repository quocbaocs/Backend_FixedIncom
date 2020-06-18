from django.db import models
import datetime

# Create your models here.
class Treasury_Yield(models.Model):
    asset_code = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    maturity = models.DateField(default=datetime.date.today, blank=True)
    issuedate = models.DateField(default=datetime.date.today, blank=True)
    couponrate = models.CharField(max_length=32)
    price = models.CharField(max_length=32)
    yeild = models.CharField(max_length=32)
