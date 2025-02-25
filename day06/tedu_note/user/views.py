from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import User
import hashlib
# Create your views here.
def reg_view(request):
    #注册
    if request.method == 'GET':
        # get 返回页面
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        #post 处理提交数据
        username = request.POST['username']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']
        #1，两个密码保持一致
        if password_1 != password_2:
            return HttpResponse('两个密码不一致！')
        #哈希算法 -- 给定明文，计算出一段定长的，不可逆的值
        #特点：1 定长输出，哈希值都是定长的，md5-32位16进制；2 不可逆：无法反向计算对应明文；3 雪崩效应：输入改变，输出必然变化
        #场景：1 密码处理；2 文件完整性校验
        #如何使用
        m = hashlib.md5()
        m.update(password_1.encode())#.encode可以把字符串变成字节串
        password_m = m.hexdigest()

        #2，当前用户名是否重复
        old_users = User.objects.filter(username=username)
        if old_users:
            return HttpResponse('用户名已注册')
        #3，插入数据【明文处理密码】
        try:
            user = User.objects.create(username=username, password=password_m)
        except Exception as e:
            #有可能 报错 - 重复插入【唯一索引注意并发写入问题】
            print('---create user error %s'%(e))
            return HttpResponse('用户名已注册')
        #4，免登陆一天
        request.session['username'] = username
        request.session['uid'] = user.id
        #TODO 修改session存储时间为一天
        request.session.set_expiry(86400)  # 设置会话过期时间为 86400 秒（1 天）

        return HttpResponseRedirect('/index/index')

def login_view(request):

    if request.method == 'GET':
        #获取登录页面
        #检测登录状态，如果登陆了，显示‘已登录’
        if request.session.get('username') and request.session.get('uid'):
            # return HttpResponse('已登录')
            return HttpResponseRedirect('/index/index')
        #检测cookies
        c_username = request.COOKIES.get('username')
        c_uid = request.COOKIES.get('uid')
        if c_username and c_uid:
            #回写session
            request.session['username'] = c_username
            request.session['uid'] = c_uid
            # return HttpResponse('已登录')
            return HttpResponseRedirect('/index/index')
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        #处理提交数据
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)#从数据库中找到的
        except Exception as e:
            print('---login user error %s'%(e))
            return HttpResponse('用户名或密码错误')

        #比对密码
        m = hashlib.md5()
        m.update(password.encode())
        password_m = m.hexdigest()
        if password_m != user.password:
            return HttpResponse('用户名或密码错误')

        #记录会话状态
        request.session['username'] = username
        request.session['uid'] = user.id

        # resp = HttpResponse('登录成功！')
        resp = HttpResponseRedirect('/index/index')
        #判断用户是否点选了‘记住用户名’
        if 'remember' in request.POST:
            # 点选了->Cookies存储username，uid时间3天
            resp.set_cookie('username', username, 3600*24*3)
            resp.set_cookie('uid', user.id, 3600*24*3)

        return resp

def logout_view(request):
    # 创建响应对象
    response = HttpResponseRedirect('/index/index')
    if 'username' in request.session:
        del request.session['username']
    if 'uid' in request.session:
        del request.session['uid']
    if 'username' in request.COOKIES:
        response.delete_cookie('username')
    if 'uid' in request.COOKIES:
        response.delete_cookie('uid')
    return response
