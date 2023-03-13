from django.urls import path
from .views import *

urlpatterns = [
    path('add_store/', add_store),
    path('get_store_by_user_token/', get_store_by_user_token),
    path('edit_store/', edit_store),
    path('send_code/', send_code),
    path('delete_sotre_by_code/', delete_sotre_by_code),
    path('get_all_stores_data/', get_all_stores_data),
]
