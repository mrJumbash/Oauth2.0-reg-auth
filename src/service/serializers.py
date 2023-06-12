from rest_framework import serializers
from service.models import Product, Category
from accounts.models import User
from accounts.serializers import LoginSerializer
from common.models import BaseModel
class GlobalSearchSerializer(serializers.Serializer):      
    def to_native(self, obj):      
        if isinstance(obj, Product):          
            serializer = ProductSerializer(obj)      
        elif isinstance(obj, User):         
            serializer = LoginSerializer(obj)
        elif isinstance(obj, Category):
            serializer = CategorySerializer(obj)                  
        else:         
            raise Exception("Neither a Product nor Category nor User instance!")      
        return serializer.data

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)

class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False)
    price = serializers.IntegerField(max_value=255)
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        return Product.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.price = validated_data.get("price", instance.price)
        instance.save()
        return instance
