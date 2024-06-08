from django.urls import path, re_path
from registeration import views

app_name = 'registeration'
urlpatterns = [path('new_user', views.new_user),
               path('get_profile_data', views.get_profile_data),
               path('add_user_photo', views.add_user_photo)
               ]
