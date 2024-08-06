from django.urls import path
from carts import views

urlpatterns = [
    path('', views.summary_cart, name='cart_summary'),
    path('add/', views.add_cart, name='cart_add'),
    path('delete/', views.delete_cart, name='cart_delete'),
    path('update/', views.update_cart, name='cart_update'),

]