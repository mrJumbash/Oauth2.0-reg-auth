from django.contrib.auth import authenticate
from accounts.models import User
from accounts.services import UserService
import random
from rest_framework.exceptions import AuthenticationFailed
from core.settings.env_reader import env


def generate_username(name):
    username = "".join(name.split(" ")).lower()
    if not User.objects.filter(username=username).exists():
        return username
    else:
        random_username = username + str(random.randint(0, 1000))
        return generate_username(random_username)


def get_username(name):
    username = "".join(name.split(" ")).lower()
    if User.objects.filter(username=username).exists():
        return username
    else:
        raise ValueError("Username does not exist")


def register_social_user(provider, user_id, email, name):
    filtered_user_by_email = User.objects.filter(email=email)

    if filtered_user_by_email.exists():
        username = get_username(name)
        registered_user = authenticate(
            username=username, password=env("GOOGLE_CLIENT_SECRET")
        )

        return {
            "username": registered_user.username,
            "email": registered_user.email,
            "tokens": UserService.tokens(user=registered_user),
        }

    else:
        username = generate_username(name)
        user = User.objects.create_user(
            username=username, email=email, password=env("GOOGLE_CLIENT_SECRET")
        )
        user.is_verified = True
        user.auth_provider = provider
        user.role = 2
        user.save()

        new_user = authenticate(username=username, password=env("GOOGLE_CLIENT_SECRET"))
        return {
            "email": new_user.email,
            "username": new_user.username,
            "tokens": UserService.tokens(user=new_user),
        }
