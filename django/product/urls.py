from django.urls import path
from .views import *

urlpatterns = [
    path('add_product/', add_product , name='Add Product'),
    path('get_all_product_data/', get_all_product_data, name='Get All Product Data'),
    path('edit_product/', edit_product, name = 'Edit Product'),
    path('get_product_by_id/<int:id>', get_product_by_id, name = 'Get Product'),
    path('get_product_by_subcat_id/<int:subcategory_id>', get_product_by_subcat_id, name = 'Get Product Subcategory'),
    path('delete_product_by_id/<int:id>', delete_product_by_id, name = 'Delete Product By ID'),
    path('add_image/', add_image, name = 'Add Image'),
    path('filter_products/', filter_products, name = 'Filter Products'),

]
