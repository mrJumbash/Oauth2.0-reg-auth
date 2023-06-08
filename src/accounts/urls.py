from django.urls import path
from accounts import views

urlpatterns = [
    path("set/tenant/", views.TenantSetAPI.as_view(), name='tenant-setting'),
    path("register/buyer/", views.RegistrationBuyerAPI.as_view(), name='register-buyer'),
    path("register/admin/", views.RegistrationAdminAPI.as_view(), name='register-admin'),
    path("register/confirm/", views.ConfirmAPIView.as_view(), name='confirm'),
    path("login/", views.LoginAPI.as_view()),
]
