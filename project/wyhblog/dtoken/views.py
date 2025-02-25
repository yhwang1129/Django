import json
import time

import jwt
from django.http import JsonResponse
from django.shortcuts import render
from user.models import UserProfile
import hashlib
from django.conf import settings

#异常码10200-10299
# Create your views here.
def tokens(request):

    if request.method != 'POST':
        result = {'code':10200, 'error':'Please use POST method'}
        return JsonResponse(result)
    json_str = request.body
    json_obj = json.loads(json_str)
    username = json_obj['username']
    password = json_obj['password']
    #校验用户名和密码
    try:
        user = UserProfile.objects.get(username=username)
    except Exception as e:
        result = {'code':10201, 'error':'The username or password is incorrect'}
        return JsonResponse(result)

    p_m = hashlib.md5()
    p_m.update(password.encode())
    if p_m.hexdigest() != user.password:
        result = {'code':10202, 'error':'The username or password is incorrect'}
        return JsonResponse(result)

    #记录会话状态
    token = make_token(username)
    result = {'code':200, 'username':username, 'data':{'token':token}}
    return JsonResponse(result)

def make_token(username, expire=3600*24):  # 定义生成 JWT 的函数，接收用户名和过期时间

    key = settings.JWT_TOKEN_KEY  # 从设置中获取密钥，用于加密 JWT
    now_t = time.time()  # 获取当前时间的时间戳（秒）
    payload_data = {'username': username, 'exp': now_t + expire}  # 创建包含用户名和过期时间的有效负载
    return jwt.encode(payload_data, key, algorithm='HS256')  # 编码有效负载为 JWT，返回生成的令牌
