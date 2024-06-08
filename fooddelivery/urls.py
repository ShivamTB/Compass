from django.urls import path, re_path
from fooddelivery import views
from django.conf.urls.static import static
from Compass.settings import STATIC_ROOT

app_name = 'fooddelivery'
urlpatterns = [path('get_restaurants', views.get_restaurants),
               path('get_filter_values', views.get_filter_values),
               path('get_menu_items', views.get_menu_items),
               path('create_order', views.create_order)
               ] + static("static/", document_root=STATIC_ROOT)
