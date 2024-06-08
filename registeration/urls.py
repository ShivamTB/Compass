from django.urls import path, re_path
from registeration import views
from django.conf.urls.static import static
from Compass.settings import STATIC_ROOT


app_name = 'registeration'
urlpatterns = [path('new_user', views.new_user),
               path('get_profile_data', views.get_profile_data),
               path('add_user_photo', views.add_user_photo),
               path('get_user_photos', views.get_user_photos)
               ] + static("static/", document_root=STATIC_ROOT)
