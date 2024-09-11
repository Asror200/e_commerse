from django.urls import path
from cart import views
from products.views_.views import detail
urlpatterns = [
    path('', views.summary_cart, name='summary_cart'),
    path('add/<slug:product_slug>/', views.add_cart, name='add_cart'),
    path('delete/', views.delete_cart, name='delete_cart'),
    path('update/', views.update_cart, name='update_cart'),
    path('detail/<slug:product_slug>/', detail, name='detail'),

]