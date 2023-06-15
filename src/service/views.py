from django.db.models import Case, When, Value, CharField
from rest_framework import generics
from service.serializers import PreferedProductSerializer,ProductSerializer, ReviewSerializer, PreferencesSerializer, ViewHistorySerializer
from service.permissions import IsTenantAndAdminOrReadOnly, IsOwnerOrReadOnly
from service.models import Product, Review, ViewHistory, Preferences
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
'''Products API'''



class ProductAPI(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsTenantAndAdminOrReadOnly]
    
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous is not True:
            queryset = Product.objects.annotate(
                priority=Case(
                    When(preferences__user=request.user, then=Value('high')),
                    default=Value('low'),
                )
            ).order_by('priority')
            serializer = PreferedProductSerializer(queryset, many=True)
            return Response(serializer.data) 
            
        return self.list(request, *args, **kwargs)


class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = "id"
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = PageNumberPagination
    
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous is not True:
            product_id = kwargs.get('id')
            ViewHistory.objects.create(product_id=product_id, user=request.user)
        return self.retrieve(request, *args, **kwargs)

'''Review API'''
class ReviewAPI(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class ReviewDetailAPI(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly]



'''List of Preferences and ViewHistory'''


class PreferencesAPI(generics.ListCreateAPIView):
    serializer_class = PreferencesSerializer
    queryset = Preferences.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination
    

class ViewHistoryAPI(generics.ListAPIView):
    serializer_class = ViewHistorySerializer
    queryset = ViewHistory.objects.all()
    permission_classes = [IsAdminUser]
    pagination_class = PageNumberPagination 
