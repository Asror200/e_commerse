from django.urls import path
from products import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:_id>', views.detail, name='detail'),
    path('detail/<int:_id>', views.detail, name='detail'),
    path('product/<int:product_id>/', views.product_comment, name='product_comment'),
    path('product/<int:product_id>/', views.product_order, name='product_order'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)