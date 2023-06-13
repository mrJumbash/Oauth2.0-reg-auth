from rest_framework import generics
from service.serializers import ProductSerializer
from service.permissions import IsTenantAndAdminOrReadOnly, IsOwnerOrReadOnly
from service.models import Product
from rest_framework.views import APIView
from accounts.models import User
from rest_framework.response import Response


class ProductAPI(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsTenantAndAdminOrReadOnly]


class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = "id"
    permission_classes = [IsOwnerOrReadOnly]

