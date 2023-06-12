from typing import Iterable, Optional
from django.db import models
from common.models import BaseModel
from accounts.models import User
from django.core.validators import MaxValueValidator

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

        
        
           
    def __str__(self) -> str:
        return self.title
