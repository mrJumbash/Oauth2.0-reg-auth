from django.contrib import admin
from service import models
from django.db.models import QuerySet

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['name']
    readonly_fields = ['created_at', 'id']
    
    
    
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "price", "id", 'category']
    readonly_fields = ["created_at", "id"]
    fields = ["title", "description", "price", "created_at", "owner", 'category']
    
    raw_id_fields = ['category']
    
    def get_queryset(self, request) -> QuerySet[models.Product]:
        queryset = super().get_queryset(request)
        queryset = queryset.select_related("category")
        return queryset