from django.db import models
from django.utils import timezone

# Postはテーブル名？
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


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
            