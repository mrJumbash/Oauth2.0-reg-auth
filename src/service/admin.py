from django.contrib import admin
from service import models
from django.db.models import QuerySet


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    fields = ["name"]
    readonly_fields = ["created_at", "id"]

@admin.register(models.Preferences)
class PreferencesAdmin(admin.ModelAdmin):
    list_display = ['product_category', 'user', 'product']
    fields = ["user", "product_category", 'product'] 
    readonly_fields = ["created_at", "id"]
     
    raw_id_fields = ["product_category", 'user', 'product']

    def get_queryset(self, request) -> QuerySet[models.Preferences]:
        queryset = super().get_queryset(request)
        queryset = queryset.select_related("product_category", 'user', 'product')
        return queryset


@admin.register(models.ViewHistory)
class ViewHistoryAdmin(admin.ModelAdmin):
    list_display = ['product', 'user']
    fields = ["user", "product"] 
    readonly_fields = ["created_at", "id"]
     
    raw_id_fields = ["product", 'user']

    def get_queryset(self, request) -> QuerySet[models.ViewHistory]:
        queryset = super().get_queryset(request)
        queryset = queryset.select_related("product", 'user')
        return queryset
    
@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["text", "product", "rating"]

    readonly_fields = ["created_at", "id"]

    fields = ["text", "product", "rating"]

    raw_id_fields = ["product"]

    def get_queryset(self, request) -> QuerySet[models.Review]:
        queryset = super().get_queryset(request)
        queryset = queryset.select_related("product")
        return queryset


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "price", "category", "discount_percentage"]
    readonly_fields = ["created_at", "id"]
    fields = [
        "title",
        "description",
        "price",
        "created_at",
        "owner",
        "category",
        "discount_percentage",
    ]

    raw_id_fields = ["category"]

    def get_queryset(self, request) -> QuerySet[models.Product]:
        queryset = super().get_queryset(request)
        queryset = queryset.select_related("category")
        return queryset
