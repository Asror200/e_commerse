from django.urls import path
from products import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('', views.home, name='home'),
                  path('about/', views.about, name='about'),
                  path('category/<int:_id>', views.home, name='category'),
                  path('detail/<int:_id>', views.detail, name='detail'),
                  path('comment/<int:_id>/', views.add_comment, name='product_comment'),
                  path('order/<int:_id>/', views.add_order, name='product_order'),
                  path('exspensive-products/', views.expensive, name='expensive'),
                  path('cheap-products/', views.cheap, name='cheap'),
                  path('rating/', views.ratings, name='rating'),
                  path('Redister-page/', views.register_user, name='register'),
                  path('login-page/', views.login_user, name='login'),
                  path('logout-page/', views.logout_user, name='logout'),
                  path('delete-product/<int:_id>/', views.delete_product, name='delete_product'),
                  path('update-product/<int:_id>/', views.update_product, name='edit_product'),
                  path('add-product/', views.add_product, name='add_product'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
