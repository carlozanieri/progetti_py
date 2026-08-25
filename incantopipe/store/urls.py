# store/urls.py
# store/urls.py
from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('categoria/<slug:category_slug>/', views.product_list, name='category_products'),
    path('pipe/<slug:slug>/', views.product_detail, name='product_detail'),
]

