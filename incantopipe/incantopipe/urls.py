# incantopipe/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("store.urls")),  # Senza namespace per ora
    path("cart/", include("cart.urls")),
    path("orders/", include("orders.urls")),
    path("payment/", include("payment.urls")),
    path("admin/", admin.site.urls),
]