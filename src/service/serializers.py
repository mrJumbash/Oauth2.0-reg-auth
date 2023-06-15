from rest_framework import serializers
from service.models import Product, Review, Preferences, Category
from rest_framework.exceptions import ValidationError


class PreferedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False)
    price = serializers.IntegerField()
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    discount_percentage = serializers.IntegerField()
    category_id = serializers.IntegerField()
    
    def category_id_validate(self, category_id):
        try:
            Category.objects.get(category_id=category_id)
        except Category.DoesNotExist:
            return ValidationError('Category does not exist')  

    def create(self, validated_data):
        return Product.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.price = validated_data.get("price", instance.price)
        instance.discount_percentage = validated_data.get('discount_percentage', instance.discount_percentage)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance
    
class ReviewSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=255)
    rating = serializers.IntegerField()
    product_id = serializers.IntegerField()
    
    def create(self, validated_data):
        return Review.create(validated_data)

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.product_id = validated_data.get('product_id', instance.product_id)
        instance.save()
        return instance


'''Preferences & ViewHistory Serializer'''
class PreferencesSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    product_category_id = serializers.IntegerField()
    product_id =serializers.IntegerField()
    
    def product_id_validate(self, product_id):
        try:
            Preferences.objects.get(product_id=product_id)
        except Preferences.DoesNotExist:
            return ValidationError('Product does not exist') 
        
    def product_category_id_validate(self, product_category_id):
        try:
            Preferences.objects.get(product_category_id=product_category_id)
        except Preferences.DoesNotExist:
            return ValidationError('Category does not exist') 
        
class ViewHistorySerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    product_id =serializers.IntegerField()
    created_at = serializers.DateTimeField(required=False)