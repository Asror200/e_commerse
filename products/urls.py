from django.urls import path
from products import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('', views.home, name='home'),
                  path('category/<int:_id>', views.category_list, name='category'),
                  path('detail/<int:_id>', views.detail, name='detail'),
                  path('product/<int:product_id>/', views.product_comment, name='product_comment'),
                  path('product/<int:product_id>/', views.product_order, name='product_order'),
                  path('about/', views.about, name='about'),
                  path('all-products/', views.home, name='index'),
                  path('exspensive-products/', views.expensive, name='expensive'),
                  path('cheap-products/', views.cheap, name='cheap'),
                  path('rating/', views.ratings, name='rating'),
                  path('Redister-page/', views.register_user, name='register'),
                  path('Redister-page/', views.register_user, name='register'),
                  path('login-page/', views.login_user, name='login'),
                  path('logout-page/', views.logout_user, name='logout'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
