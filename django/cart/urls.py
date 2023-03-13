from django.urls import path
from .views import *


urlpatterns = [
    #Cart
    path('add_to_cart/',add_to_cart),
    path('get_cart_by_token/',get_cart_by_token),
    path('edit_cart_data/',edit_cart_data),
    path('delete_item_in_cart/',delete_item_in_cart),
    # path('delete_user_cart_by_cart_id/',delete_user_cart_by_cart_id),
    
]