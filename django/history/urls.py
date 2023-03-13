from django.urls import path
from .views import *

urlpatterns = [
    #Comments
    path('add_comment/',add_comment),
    path('add_rate/',add_rate),
    path('get_all_comments_data/',get_all_comments_data),
    path('get_product_commet_by_id/<int:product_id>',get_product_commet_by_id),
    path('delete_comment_by_id/<int:id>',delete_comment_by_id),
    
    # #Likes
    # path('add_like/',add_like),
    # path('get_all_like_by_product_id/<int:product_id>',get_all_like_by_product_id),
    # path('delete_like_by_id/<int:id>',delete_like_by_id),
    
    #Favorites
    path('get_all_favorites_data/',get_all_favorites_data),
    path('add_favorites/',add_favorites),
    path('delete_favorites_by_id/<int:id>',delete_favorites_by_id),
    # path('edit_favorites/',edit_favorites),
]