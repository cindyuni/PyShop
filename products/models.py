# 定義資料欄位
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)  # CharField是可以接受文字類型的輸入
    price = models.FloatField()  # FloatField是可以接受float類型的輸入
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=225)
    discount = models.FloatField()

