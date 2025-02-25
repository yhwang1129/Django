import json
import random

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from .models import UserProfile
import hashlib
from tools.logging_dec import logging_check
from django.core.cache import cache
from tools.sms import YunTongxin
from django.conf import settings
from .tasks import send_sms_c
#异常码 10100-10199

#django提供一个装饰器 method_decorator,可以将函数装饰器转换成方法装饰器

# Create your views here.
#FBV
@logging_check
def users_views(request, username):

    if request.method != 'POST':
        result = {'code':10103, 'error':'Please use POST'}
        return JsonResponse(result)

    user = request.myuser
    avatar = request.FILES['avatar']
    user.avatar = avatar
    user.save()
    return JsonResponse({'code':200})


#CBV 更灵活【可继承】
class UserViews(View):

    def get(self, request, username=None):

        if username:
            #v1/users/wyh
            try:
                user = UserProfile.objects.get(username=username)
            except Exception as e:
                result = {'code':10102, 'error':'The username is wrong'}
                return JsonResponse(result)
            result = {'code':200, 'username':username, 'data':{'info':user.info, 'sign':user.sign, 'nickname':user.nickname, 'avatar':str(user.avatar)}}
            return JsonResponse(result)
        else:
            #v1/users
            pass
        return JsonResponse({'code': 200, 'msg': 'test'})

    def post(self, request):

        json_str = request.body
        json_obj = json.loads(json_str)
        username = json_obj['username']
        email = json_obj['email']
        password_1 = json_obj['password_1']
        password_2 = json_obj['password_2']
        phone = json_obj['phone']
        sms_num = json_obj['sms_num']

        #参数基本检查
        if password_1 != password_2:
            result = {'code':10100, 'error':'The two passwords do not match'}
            return JsonResponse(result)

        #比对验证码
        old_code = cache.get('sms_%s'%(phone))
        if not old_code:
            result = {'code':10110, 'error':'The code is wrong'}
            return JsonResponse(result)
        if int(sms_num) != old_code:
            result = {'code':10111, 'error':'The code is wrong'}
            return JsonResponse(result)

        #检测用户名是否可用
        old_users = UserProfile.objects.filter(username=username)
        if old_users:
            result = {'code':10101, 'error':'The username is already taken'}
            return JsonResponse(result)
        #UserProfile插入数据（密码md5存储）
        p_m = hashlib.md5()
        p_m.update(password_1.encode())

        UserProfile.objects.create(username=username, nickname=username, password=p_m.hexdigest(), email=email, phone=phone)

        result = {'code':200, 'username':username, 'data':{}}
        return JsonResponse(result)

        pass

    @method_decorator(logging_check)
    def put(self, request, username=None):
        #更新用户数据【昵称，个人签名，个人描述】
        json_str = request.body
        json_obj = json.loads(json_str)

        user = request.myuser

        user.sign = json_obj['sign']
        user.info = json_obj['info']
        user.nickname = json_obj['nickname']

        user.save()
        return JsonResponse({'code':200})

def sms_view(request):

    if request.method != 'POST':
        result = {'code':10108, 'error':'Please use POST method'}
        return JsonResponse(result)

    json_str = request.body
    json_obj = json.loads(json_str)
    phone = json_obj['phone']
    #生成随机验证码
    code = random.randint(1000, 9999)
    print('phone', phone, 'code', code)
    #存储随机码django_redis
    cache_key = 'sms_%s' % (phone)
    #检查是否有已经发过且未过期
    old_cache = cache.get(cache_key)
    if old_cache:
        return JsonResponse({'code':10112, 'error':'The code is already existed'})
    cache.set(cache_key, code, 60)
    # #发送随机吗->短信
    # send_sms(phone, code)

    #celery版
    send_sms_c.delay(phone, code)

    return JsonResponse({'code':200})

def send_sms(phone, code):

    config = settings.SMS_CONFIG

    yun = YunTongxin(**config)
    res = yun.run(phone, code)