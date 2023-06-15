from service.models import Product


class ProductService:
    __product_model = Product

    @property
    def product_model(self):
        return self.__product_model
