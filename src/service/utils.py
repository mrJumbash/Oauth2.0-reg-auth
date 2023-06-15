from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User


def send_products_via_email(email):
    subject = "Our products has been decreased"
    message = f"These products were decreased"
    email_from = settings.EMAIL_HOST
    send_mail(subject, message, email_from, [email])
