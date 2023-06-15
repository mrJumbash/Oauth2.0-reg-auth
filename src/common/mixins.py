from service.models import Product, Category
from accounts.models import User
from service.serializers import ProductSerializer, CategorySerializer
from accounts.serializers import LoginSerializer
from django.db.models import Q


class GlobalSearchMixin:
    def global_querylist(self, qeurylist, search):
        qeurylist = (
            {
                "queryset": Product.objects.filter(
                    Q(title__icontains=search) | Q(price__icontains=search)
                ),
                "serializer_class": ProductSerializer,
            },
            {
                "queryset": User.objects.filter(Q(username__icontains=search)),
                "serializer_class": LoginSerializer,
            },
            {
                "queryset": Category.objects.filter(Q(name__icontains=search)),
                "serializer_class": CategorySerializer,
            },
        )

        return qeurylist
