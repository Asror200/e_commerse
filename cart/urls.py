from django.urls import path
from . import views

urlpatterns = [
    path('', views.summary_cart, name='summary_cart'),
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('delete/', views.delete_cart, name='delete_cart'),
    path('update/', views.update_cart, name='update_cart'),

]