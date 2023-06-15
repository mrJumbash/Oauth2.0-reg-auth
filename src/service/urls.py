from django.urls import path
from service import views

urlpatterns = [
    path("products/", view=views.ProductAPI.as_view()),
    path("products/<uuid:id>/", view=views.ProductDetailAPI.as_view()),
    
    path('reviews/', view=views.ReviewAPI.as_view()),
    path('reviews/<uuid:id>', view=views.ReviewDetailAPI.as_view())
]
