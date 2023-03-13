from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from product.models import ProductModel

 # Create your views here.


@api_view(['GET'])
# @permission_classes([AllowAny])
def get_cart_by_token(request):
    user = request.user
    cart = Cart_Model.objects.filter(user_id=user.id).first()
    serializered = Cart_Serializers(cart).data 
    return Response({"Cart":serializered, "status":status.HTTP_200_OK})



# @api_view(['GET'])
# # @permission_classes([AllowAny])
# def get_cart_by_token(request):
#     user = request.user
#     cart_data = Cart_Model.objects.filter(user_id=user.id).first()
#     items = Cart_Item_Model.objects.filter(cart_id=cart_data.id)
#     item_list = Cart_Item_Serializer(items, many=True).data
#     if len(item_list) == 1:
#         if item_list[0]['quantity'] == 1:
#             cart_data.total_price = total_price
#             cart = Cart_Serializers(cart_data).data
#             return Response({"Cart Details":cart,"item_list":item_list, "status":status.HTTP_200_OK})
#         if item_list[0]['quantity'] > 1:
#             total_price =items.product.price * items.quantity
#             cart_data.total_price = total_price
#             return Response({"Cart Details":cart, "item_list":item_list, "status":status.HTTP_200_OK})
#     elif len(items) > 1:
#         for item in item_list:
#             for i in item:
#                 total_price = total_price + i.product.price
#                 cart['total_price'] = total_price
#         return Response(cart, status=status.HTTP_200_OK)
#     else:
#         return Response("there is no item in the cart", status=status.HTTP_204_NO_CONTENT)
    



"""Add Product to Cart"""
@api_view(['POST'])
# @permission_classes([AllowAny])
def add_to_cart(request):
    user = request.user
    c_data = request.data
    Should_increase_the_count = False
    if "Should_increase_the_count" in c_data:
        Should_increase_the_count = c_data["Should_increase_the_count"]
    if user is None:
        return Response('لطفا ثبت نام کنید', status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    else:
        cart_check = Cart_Model.objects.filter(user_id=user.id).first()
        product_check = ProductModel.objects.filter(pk=c_data['product']).first()
        cart_item = Cart_Item_Model.objects.filter(cart=cart_check,product=product_check).first()
        if cart_item is None:
            c_data['cart'] = cart_check.id
            if 'quantity' in c_data:
                pass
            else:
                c_data['quantity'] = 1
            c_data_serializer = Cart_Item_Serializer(data=c_data)
            if c_data_serializer.is_valid():
                c_data_serializer.save()
                return Response(c_data_serializer.data, status=status.HTTP_201_CREATED)
            return Response(c_data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            if Should_increase_the_count == False:
                return Response('این ایتم از قبل در سبد خرید شما موجود است')
            if 'quantity' in c_data:
                cart_item.quantity = cart_item.quantity + c_data['quantity']
            else:
                cart_item.quantity = cart_item.quantity + 1
            cart_item.save()
            c_data_serializer = Cart_Item_Serializer(cart_item)
            return Response(c_data_serializer.data, status=status.HTTP_200_OK)





@api_view(['POST'])
# @permission_classes([AllowAny])
def edit_cart_data(request):
    user= request.user
    c_data = request.data
    found_cart = Cart_Model.objects.filter(user_id=user.id).first()
    c_data['cart'] = found_cart.id
    data_found = Cart_Item_Model.objects.filter(product_id=c_data['product']).first()
    if data_found is None:
        return Response("product with that id does not exist", status=status.HTTP_404_NOT_FOUND)
    serializer = Cart_Item_Serializer(data_found, c_data, partial=True)
    if serializer.is_valid():
        serializer.save()   
        return Response({"massage":'مشخصات ایتم با موفقیت تغییر یافت', "payload": serializer.data}, status=status.HTTP_206_PARTIAL_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
# @permission_classes([AllowAny])
def delete_item_in_cart(request):
    user = request.user
    item_id = request.data['product']
    cart_found = Cart_Model.objects.filter(user_id=user).first()
    item_found = Cart_Item_Model.objects.filter(product_id=item_id, cart_id=cart_found.id).first()
    if not item_found:
        return Response('محصول یافت نشد', status=status.HTTP_404_NOT_FOUND)
    else:
        item_found.delete()
        return Response('محصول با موفقیت حذف شد', status=status.HTTP_410_GONE)
        
        

    


