from django.db import models
from django.utils import timezone

class CompanyAssets(models.Model):
    # カラム定義
    item_name = models.CharField(max_length=100)
    purchas_date = models.CharField(max_length=10)
    buyer = models.CharField(max_length=30)
    jungle = models.CharField(max_length=1)
    memo = models.CharField(max_length=500)
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            default=timezone.now)
            