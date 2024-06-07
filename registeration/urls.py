from django.urls import path, re_path
from registeration import views

app_name = 'registeration'
urlpatterns = [path('new_user', views.new_user),
               path('get_referral_count', views.get_referral_count),
               path('get_referral_id', views.get_referral_id),
               ]
