from celery import shared_task
from service.utils import send_products_via_email
import time

@shared_task
def set_price(product_id):
    from service.models import Product
    from accounts.models import User
    product = Product.objects.get(id=product_id)
    new_price = (product.price - product.price * product.discount_percentage / 100)
    product.price = new_price
    product.save()
    
    users = User.objects.all()
    
    email_list = [user.email for user in users]
    for email in email_list:
        send_products_via_email(email)
    
    