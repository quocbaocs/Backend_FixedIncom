from django.db import models

# Create your models here.
class Treasury_Yield(models.Model):
    bondName = models.CharField(max_length=32)
    
    couponRate = models.CharField(max_length=32)

    bondPrice = models.CharField(max_length=32)

    bondYield = models.CharField(max_length=32)
