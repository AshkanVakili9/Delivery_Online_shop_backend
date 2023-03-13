from django.contrib.auth import authenticate
from django.core.files.base import ContentFile
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from cart.models import Cart_Model
import random
import requests
import json
import base64


@api_view(["POST"])
@permission_classes([AllowAny])
def add_user(request):
    user_data = request.data
    serializer = UserSerializer(data=user_data)
    user_check = UserModel.objects.filter(phone=request.data["phone"]).first()
    if user_check is not None:
        return Response("کاربر با این شماره موبایل موجود است شماره دیگری را وارد کنید", status=status.HTTP_208_ALREADY_REPORTED)
    elif serializer.is_valid():
        unique_id = str(random.randint(100000, 999999))
        url = 'https://api.sms.ir/v1/send/verify'
        headers = {
            'X-API-KEY': 'xLaqtCB7xkF6N4HB3OBSHbfPxZlMd8VXbpSOAuv3vFU5EPaTZcPqVMLhZw0lIvEW',
            'ACCEPT': 'application/json',
            'Content-Type': 'application/json'}
        sms_data = {"mobile": request.data["phone"], "templateId": 358538,
                    "parameters": [{"name": "CODE", "value": unique_id}]}
        requset_sms = requests.post(
            url=url, headers=headers, data=json.dumps(sms_data), params=request.POST)
        sms_data = {"phone": user_data["phone"], "sms": unique_id}
        sms_data_ser = SmsSerializer(data=sms_data)
        if sms_data_ser.is_valid():
            sms_data_ser.save()
            serializer.save()
            user = UserModel.objects.filter(phone=user_data["phone"]).first()
            token = Token.objects.create(user=user)
        return Response({"massage": "user created, and sms sent successfully", "payload": serializer.data, "token": str(token)}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def check_verify_code(request):
    user = request.user
    code = request.data['code']
    info = SmsModel.objects.filter(phone=user.phone).first()
    if info is not None:
        if info.sms == code:
            user.is_verifed = True
            user.save()
            info_delete = SmsModel.objects.get(phone=user.phone)
            info_delete.delete()
            cart = Cart_Model.objects.create(user=user)
            cart.save()
            return Response("sms is true", status=status.HTTP_200_OK)
        return Response("sms is Not true", status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("phone Number in Not true", status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def check_code_change_password(request):
    user_get = request.user
    code = request.data['code']
    new_password = request.data['new_password']
    sms = SmsModel.objects.filter(phone=user_get.phone).first()
    if sms is not None:
        if sms.sms == code:
            sms_delete = SmsModel.objects.get(phone=user_get.phone)
            sms_delete.delete()
            user_get.set_password(new_password)
            user_get.save()
            return Response("password have been updated", status=status.HTTP_200_OK)
        return Response("sms is not true", status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("sms has not been sent", status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def login_user(request):
    user_get = request.user
    password = request.data['password']
    if user_get.check_password(password):
        if user_get.is_verifed == True:
            serializer = UserSerializer(user_get)
            return Response({"response": "correct Password", "payload": serializer.data, "token": str(request.auth)}, status=status.HTTP_200_OK)
        return Response('sms check has not been completed', status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    return Response('user password is wrong ', status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def check_token(request):
    user = request.user
    if user is not None:
        serializer = UserSerializer(user)
        return Response({"payload": serializer.data}, status=status.HTTP_200_OK)
    return Response({"massage": "user does not exist"}, status=status.HTTP_400_BAD_REQUEST)


# def updateUser(user, edit_data):
#     if "first_name" in edit_data:
#         user.first_name = edit_data["first_name"]
#     if "last_name" in edit_data:
#         user.last_name = edit_data["last_name"]
#     if "password" in edit_data:
#         user.set_password(edit_data["password"])
#     if "address" in edit_data:
#         user.address = edit_data["address"]
#     if "image" in edit_data:
#         string = edit_data["image"]
#         string = string.split("base64,")[1]
#         decoded_file = base64.b64decode(string)
#         image = ContentFile(decoded_file)
#         user.image = image
#     return user


# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def edit_user(request):
#     edit_data = request.data
#     user = request.user
#     if user is not None:
#         user = updateUser(user, edit_data)
#         user.save()
#         return Response({"massage": "اطلاعات کاربر با موفقیت تغییر یافت", "payload": UserSerializer(user).data}, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""esay way to update a user"""
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_user(request):
    user = request.user
    data = request.data
    user_found = UserModel.objects.filter(id=user.id).first()
    if user_found is None:
        return  Response('there is no user with this token ', status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user, data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response("اطلاعات با موفقیت تغییر یافت", status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_user(request):
    student_data = UserModel.objects.all()
    return Response(UserSerializer(student_data, many=True).data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_account(request):
    user_get = request.user
    code = request.data['code']
    sms = SmsModel.objects.filter(phone=user_get.phone).first()
    if sms is not None:
        if sms.sms == code:
            sms_delete = SmsModel.objects.get(phone=user_get.phone)
            sms_delete.delete()
            user_get.delete()
            return Response("account have been deleted", status=status.HTTP_200_OK)
        return Response("sms is not true", status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("sms hasent been sent", status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_sms(request):
    user = request.user
    unique_id = str(random.randint(100000, 999999))
    url = 'https://api.sms.ir/v1/send/verify'
    headers = {
        'X-API-KEY': 'xLaqtCB7xkF6N4HB3OBSHbfPxZlMd8VXbpSOAuv3vFU5EPaTZcPqVMLhZw0lIvEW',
        'ACCEPT': 'application/json',
        'Content-Type': 'application/json'
    }
    sms_data = {
        "mobile": user.phone, "templateId": 358538,
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
        return Response("Sms has been Sent", status=status.HTTP_201_CREATED)
    return Response("Sms has been NoT Sent", status=status.HTTP_201_CREATED)
