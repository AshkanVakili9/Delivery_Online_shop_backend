from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework import status, permissions
from rest_framework.response import Response
from .serializers import *
from .filters import *
from .models import *
from history.models import FavoriteModel
from history.serializers import FavoriteSerializer
from .pagination import CustomPagination
# Create your views here.


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_product_data(request):
    user = request.user
    paginator = CustomPagination()
    products = ProductModel.objects.all()
    products = paginator.paginate_queryset(products, request)
    product_data =ProductSerializer(products, many=True).data
    if user.id == None:
        for data in product_data:
            data['is_fave'] = False
        # return Response(product_data, status=status.HTTP_200_OK)
        return paginator.get_paginated_response(product_data)
    history = FavoriteModel.objects.filter(user_id=user.id)
    history = FavoriteSerializer(history, many=True).data
    if history is not None:
        for his_data in history:
            for data in product_data:
                if data['id'] == his_data['product']:
                    data['is_fave'] = True
        return paginator.get_paginated_response(product_data)
    return paginator.get_paginated_response(product_data)
        # return Response(product_data, status=status.HTTP_200_OK)
    # return Response(product_data, status=status.HTTP_200_OK)




@api_view(['POST'])
@permission_classes([AllowAny])
def add_image(request):
    if request.method == 'POST':
        p_data = request.data
        serializer = ProductImageSerializer(data=p_data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def add_product(request):
    p_data = request.data
    product_data_serializer = ProductSerializer1(data=p_data)
    if product_data_serializer.is_valid():
        product_data_serializer.save()
        return Response(product_data_serializer.data, status=status.HTTP_201_CREATED)
    return Response(product_data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def edit_product(request):
    data = request.data
    data_found = ProductModel.objects.get(id=data['id'])
    if data_found is None:
        return Response("product with that id does not exist", status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer1(data_found, data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"massage": 'مشخصات محصول با موفقیت تغییر یافت', "payload": serializer.data}, status=status.HTTP_206_PARTIAL_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_product_by_id(request, id):
    p_data = ProductModel.objects.filter(id=id)
    if not p_data:
        return Response('محصولی با مشخصات این ایدی وجود ندارد', status=status.HTTP_404_NOT_FOUND)
    else:

        return Response(ProductSerializer1(p_data, many=True).data, status=status.HTTP_302_FOUND)


@api_view(['GET'])
@permission_classes([AllowAny])
def delete_product_by_id(request, id):
    p_data = ProductModel.objects.filter(id=id)
    if not p_data:
        return Response('محصولی بااین مشخصات وجود ندارد', status=status.HTTP_404_NOT_FOUND)
    else:
        p_data.delete()
        return Response('محصول با موفقیت حذف شد', status=status.HTTP_410_GONE)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_product_by_subcat_id(request, subcategory_id):
    p_data = ProductModel.objects.filter(subcategory_id=subcategory_id)
    if not p_data:
        return Response('محصولی با زیردسته مشخصات این ایدی وجود ندارد', status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(ProductSerializer1(p_data, many=True).data, status=status.HTTP_200_OK)



@api_view(['GET'])
@permission_classes([AllowAny])
def filter_products(request):
    queryset = ProductModel.objects.all()
    filterset = PriceFilter(request.GET, queryset=queryset)
    if filterset.is_valid():
        queryset = filterset.qs
    serializer = ProductSerializer1(queryset, many=True)
    return Response(serializer.data)


# @api_view(['POST','GET'])
# @permission_classes([AllowAny])
# def filter_price(request):
#     if request.method == 'POST':
#         filter_price1 = request.data['min_value']
#         filter_price2 = request.data['max_value']
#         if filter_price1 =='':
#             filter_price1=0
#         if filter_price2=='':
#             filter_price2=ProductModel.objects.all().aggregate(Max('price'))
#         my_products = ProductModel.objects.filter(price__range=(filter_price1,filter_price2))
#         # context = { "products":my_products}
#         return Response(status=status.HTTP_200_OK)