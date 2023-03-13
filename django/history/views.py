from .models import *
from .serializers import *
from product.models import ProductModel
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
# Create your views here.




################ Comments ################

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_comments_data(request):
    comments_data = CommentsModel.objects.all()
    return Response(CommentsSerializer(comments_data, many=True).data, status=status.HTTP_200_OK)


@api_view(['POST'])
# @permission_classes([AllowAny])
def add_comment(request):
    user =request.user
    c_data = request.data
    c_data["user"]= user.id
    comment = CommentsModel.objects.filter(user_id=user).first()
    if comment is None:
        serializer = CommentsSerializer(data=c_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        serializer = CommentsSerializer(comment, c_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "your comment changed", "payload": serializer.data , "status":status.HTTP_201_CREATED})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
# @permission_classes([AllowAny])
def add_rate(request):
    user = request.user
    r_data = request.data
    counte = 1
    product = ProductModel.objects.get(id=r_data['product'])
    new_value = r_data['rate']
    user_check = RateModel.objects.filter(user=user , product_id=r_data['product']).first()
    if user_check is None: 
        r_data["user"]= user.id
        serializer = RateSerializer(data=r_data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        serializer = RateSerializer(user_check, r_data, partial=True)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    all_rates = RateModel.objects.filter(product_id=r_data['product'])
    numbers = len(all_rates)
    all_rates = [r.rate for r in all_rates]
    avg = sum(all_rates) / numbers
    product.rate = avg
    product.save()
    return Response({"massage":"your rate was submitted successfully",
                    "product_id":product.id,
                    "new_rate":product.rate,
                    }, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_product_commet_by_id(request, product_id):
    c_data = CommentsModel.objects.filter(product_id=product_id)
    product = ProductModel.objects.filter(id=product_id).first()
    if product is not None:
        if not c_data:
            return Response('there is no comments for this product id', status=status.HTTP_404_NOT_FOUND)
        return Response(CommentsSerializer(c_data, many=True).data, status=status.HTTP_200_OK)
    return Response("there is no product with this id", status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([AllowAny])
def delete_comment_by_id(request,id):
    c_data = CommentsModel.objects.filter(id=id)
    if not c_data:
        return Response('there is no comments with this id', status=status.HTTP_404_NOT_FOUND)
    else:
        c_data.delete()
        return Response('comment is deleted', status=status.HTTP_410_GONE)
        
        
        



################ Favorites ################
@api_view(['GET'])
# @permission_classes([AllowAny])
def get_all_favorites_data(request):
    user = request.user
    f_data = FavoriteModel.objects.filter(user_id=user).first()
    if f_data:
        return Response(FavoriteSerializer(f_data).data, status=status.HTTP_200_OK)
    return Response("favorite list is empty", status=status.HTTP_204_NO_CONTENT)





@api_view(['POST'])
# @permission_classes([AllowAny])
def add_favorites(request):
    user = request.user
    f_data = request.data
    f_data['user'] = user.id
    fav_check = FavoriteModel.objects.filter(user_id=f_data['user'], product_id=f_data['product']).first()
    if fav_check is None:
        serializer = FavoriteSerializer(data=f_data)
        if serializer.is_valid():
            serializer.save()
            product = ProductModel.objects.get(id=f_data['product'])
            product.is_fave = True
            product.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response("you have been add this product to your favorites before.", status=status.HTTP_302_FOUND)



@api_view(['GET'])
# @permission_classes([AllowAny])
def delete_favorites_by_id(request, id):
    user = request.user
    data= FavoriteModel.objects.filter(user=user,id=id).first()
    if data is not None:
        product = ProductModel.objects.get(id=data.product_id)
        product.is_fave = False
        product.save()
        data.delete()
        return Response("fave product have been deleted", status=status.HTTP_200_OK)
    return Response('fav is not exist or have been deleted before', status=status.HTTP_404_NOT_FOUND)







