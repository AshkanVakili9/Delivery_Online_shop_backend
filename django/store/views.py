from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import *
from .serializers import *
import random
import requests
import base64
import json


# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_stores_data(request):
    store_data = StoreModel.objects.all()
    return Response(StoreSerializer(store_data, many=True).data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_store(request):
    user_check = request.user
    if user_check.is_store == True:
        return Response("user owns a store, and can not add a store", status=status.HTTP_208_ALREADY_REPORTED)
    store_data = request.data
    serializer = StoreSerializer(data=store_data)
    if serializer.is_valid():
        serializer.save() 
        # store_data = serializer.save() 
        # store_data['user_id'] = request.user.id
        user_check.is_store = True
        user_check.save()
        return Response({"massage": "store created successfully", "payload": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_store_by_user_token(request):
    user = request.user
    store = StoreModel.objects.filter(user_id=user.id).first()
    if not store:
        return Response('فروشگاهی با مشخصات این ایدی وجود ندارد', status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(StoreSerializer2(store).data, status=status.HTTP_200_OK)


def updateStore(store, edit_data):
    if "store_name" in edit_data:
        store.store_name = edit_data["store_name"]
    if "store_phone_number" in edit_data:
        store.store_phone_number = edit_data["store_phone_number"]
    if "address" in edit_data:
        store.set_password(edit_data["address"])
    if "logo" in edit_data:
        string = edit_data["logo"]
        string = string.split("base64,")[1]
        decoded_file = base64.b64decode(string)
        image = ContentFile(decoded_file)
        user.logo = logo
    return store


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_store(request):
    edit_data = request.data
    user = request.user
    store = StoreModel.objects.filter(user_id=user.id).first()
    if store is not None:
        store = updateStore(store, edit_data)
        store.save()
        return Response({"massage": "اطلاعات فروشگاه با موفقیت تغییر یافت", "payload": StoreSerializer(store).data}, status=status.HTTP_200_OK)
    return Response('اطلاعات فروشگاه با موفقیت تغییر یافت', status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def send_code(request):
    user = request.user
    info = StoreModel.objects.filter(user_id=user.id).first()
    if info is not None:
        unique_id = str(random.randint(100000, 999999))
        url = 'https://api.sms.ir/v1/send/verify'
        headers = {
            'X-API-KEY': 'xLaqtCB7xkF6N4HB3OBSHbfPxZlMd8VXbpSOAuv3vFU5EPaTZcPqVMLhZw0lIvEW',
            'ACCEPT': 'application/json',
            'Content-Type': 'application/json'
        }
        sms_data = {
            "mobile": user.phone, "templateId": 851571,
            "parameters": [
                {
                    "name": "CODE",
                    "value": unique_id
                }
            ]
        }
        requset_sms = requests.post(
            url=url, headers=headers, data=json.dumps(sms_data), params=request.POST)
        sms_data = {"phone": user.phone, "sms": unique_id}
        sms_data_ser = SmsSerializer(data=sms_data)
        if sms_data_ser.is_valid():
            sms_data_ser.save()
        return Response('رمز فرستاده شد ', status=status.HTTP_200_OK)
    return Response("شماره موبایل درست نیست...", status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_sotre_by_code(request):
    user = request.user
    code = request.data['code']
    sms = SmsModel.objects.filter(phone=user.phone).first()
    if sms is not None:
        if sms.sms == code:
            store_account = StoreModel.objects.get(user_id=user.id)
            store_account.delete()
            del_code = SmsModel.objects.get(phone=user.phone)
            del_code.delete()
            return Response("فروشگاه حذف گردید", status=status.HTTP_200_OK)
        return Response("sms is not true", status=status.HTTP_200_OK)
    return Response("phone is not true", status=status.HTTP_200_OK)
