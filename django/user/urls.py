from django.urls import path
from .views import *

urlpatterns = [
    path('add_user/', add_user, name='add_user'),
    path("check_verify_code/", check_verify_code, name='check_verify_code'),
    path('check_token/', check_token, name= 'check_token'),
    path("login_user/", login_user, name='login_user'),
    path("check_code_change_password/", check_code_change_password, name='check_verify_code_change_password'),
    path("delete_account/", delete_account, name='delete_account'),
    path("edit_user/", edit_user, name='edit_user'),
    path("send_sms/", send_sms, name='send_sms'),
    path("get_all_user/", get_all_user, name='get_all_user'),
]
