from django.urls import path
from products.views_ import auth_views, views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import set_language
from cart.views import summary_cart

urlpatterns = [
                  path('', views.home, name='home'),
                  path('about/', views.about, name='about'),
                  path('category/<slug:category_slug>/', views.home, name='category'),
                  path('detail/<slug:product_slug>/', views.detail, name='detail'),
                  path('comment/<slug:product_slug>/', views.add_comment, name='product_comment'),
                  path('order/<slug:product_slug>/', views.add_order, name='product_order'),
                  path('Redister-page/', auth_views.register_user, name='register_page'),
                  path('login-page/', auth_views.login_user, name='login_page'),
                  path('logout-page/', auth_views.logout_user, name='logout_page'),
                  path('delete-product/<slug:product_slug>/', views.delete_product, name='delete_product'),
                  path('update-product/<slug:product_slug>/', views.update_product, name='edit_product'),
                  path('add-product/', views.add_product, name='add_product'),
                  path('i18n/setlang/', set_language, name='set_language'),
                  path('shopping-cart/', summary_cart, name='shopping_cart'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
