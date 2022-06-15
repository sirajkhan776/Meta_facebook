from django.contrib import admin
from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("registration", views.signup, name="save_info"),
    path("contact", views.contact, name="contact"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("cart", views.cartinfo, name="cartdtl"),
    path("checkout", views.checkout, name="checkout"),
    path("order", views.order_dtl, name="order"),


]
