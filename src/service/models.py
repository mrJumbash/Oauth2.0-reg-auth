from typing import Any, Iterable, Optional
from django.db import models
from common.models import BaseModel
from accounts.models import User
from django.core.validators import MaxValueValidator
from service.tasks import set_price


class Category(BaseModel):
    name = models.CharField(max_length=255, verbose_name='category_name')
    
    def __str__(self) -> str:
        return self.name


class Product(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Заголовок")

    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    
    description = models.TextField(verbose_name="Описание")
    
    discount_percentage = models.PositiveIntegerField(default=0,
                                                      validators=[MaxValueValidator(100)],
                                                      verbose_name='product_discount')

    price = models.FloatField(verbose_name="Цена")

    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__discount_percentage = self.discount_percentage
    
    def save(self, *args, **kwargs,):
        if self.discount_percentage != self.__discount_percentage:
            set_price.delay(self.id)
        return super().save(*args, **kwargs)        
           
    def __str__(self) -> str:
        return self.title
