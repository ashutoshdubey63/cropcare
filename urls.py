from django.urls import path
from.import views

urlpatterns=[
    path("",views.index),
    path("index/",views.index),
    path("aboutus/",views.about),
    path("team/",views.team),
    path("gallery/",views.gallery),
    path("category/",views.category),
    path("services/",views.services),
    path("contact/",views.contact),
    path("login/",views.login),
    path("order/",views.orders),
    path("register/",views.register),
    path("services/",views.services),
    path("cart/",views.cart),
    path("profile/",views.profile),
    path("product/",views.product),
    path("details/",views.details),
    path("dashboard/",views.dashboard),
    path("logout/",views.logout),
    path("myorders/",views.myorders),
]