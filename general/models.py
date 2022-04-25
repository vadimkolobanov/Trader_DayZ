from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Trader(models.Model):
    name = models.TextField(verbose_name='Название трейдера')
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class Category(models.Model):
    name = models.TextField(verbose_name='Категория товара')
    attach_to_trader = models.ForeignKey(Trader, on_delete=models.DO_NOTHING, verbose_name='Относится к трейдеру')
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class Item(models.Model):
    CHOICES = (
        ("*", "Максимум"),
        ("V", "Транспортное средство"),
        ("VNK", "Транспортное средство без ключа"),
        ("M", "Магазин для патронов"),
        ("W", "Оружие"),
        ("S", "Стейк из мяса"),
        ("K", "Дубликат ключа"),

    )
    class_name = models.TextField(verbose_name='Наименование товара')
    quantity = models.CharField(
        max_length=7,
        choices=CHOICES,
        default='*'
    )
    buyvalue = models.IntegerField(verbose_name="Покупка")
    sellvalue = models.IntegerField(verbose_name="Продажа")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='Относится к категории')
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
