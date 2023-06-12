from itertools import chain
from rest_framework import generics
from rest_framework.response import Response
from service.serializers import ProductSerializer, GlobalSearchSerializer
from service.models import Product, Category
from accounts.models import User
from service.permissions import IsTenantAndAdminOrReadOnly, IsOwnerOrReadOnly
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter






class ProductAPI(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsTenantAndAdminOrReadOnly]


class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = "id"
    permission_classes = [IsOwnerOrReadOnly]
