from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

POST_FORM = '''
<form method='post' action='/test_get_post'>
    用户名：<input type='text' name='uname'>
    <input type='submit' value='提交'>
</form>
'''


def page_2003_views(request):

    html = "<h1>这是第一个页面</h1>"
    return HttpResponse(html)

def index_view(request):

    html = "这是我的首页"
    return HttpResponse(html)

def page1_view(request):

    html = "这是编号为1的网页"
    return HttpResponse(html)

def page2_view(request):

    html = "这是编号为2的网页"
    return HttpResponse(html)

def pagen_view(request, pg):

    html = "这是编号为%s的网页!"%(pg)
    return HttpResponse(html)

def simple_math(request, num1, op, num2):

    result = 0
    if op not in ['add', 'sub', 'mul']:
        return HttpResponse("Your op is wrong")
    elif op == 'add':
        result = num1 + num2
    elif op == 'sub':
        result = num1 - num2
    elif op == 'mul':
        result = num1 * num2

    return HttpResponse('结果为：%s'%result)

def cal_view(request, x, op, y):
    # 转换x和y为整数
    x = int(x)
    y = int(y)

    result = 0
    if op not in ['add', 'sub', 'mul']:
        return HttpResponse("Your op is wrong")
    elif op == 'add':
        result = x + y
    elif op == 'sub':
        result = x - y
    elif op == 'mul':
        result = x * y
    return HttpResponse('结果为：%s!' % result)

def birthday_view(request, x, y, z):

    html = "出生日期为%s年%s月%s日"%(x, y, z)
    return HttpResponse(html)

def test_request(request):

    print('path info is', request.path_info)
    print('method is', request.method)
    print('querystring is', request.GET)
    print('full path is', request.get_full_path())

    return HttpResponse("test request ok")

def test_get_post(request):

    if request.method == 'GET':
        print(request.GET)
        print(request.GET['a'])
        # 问卷调查 - form get 兴趣爱好 - 复选框
        print(request.GET.getlist('a'))
        print(request.GET.get('c', 'no c'))
        return HttpResponse(POST_FORM)

    elif request.method == 'POST':
        #处理用户提交数据
        print('uname is', request.POST['uname'])
        return HttpResponse('post is ok')
    else:
        pass

    return HttpResponse("test get post is ok")

def test_html(request):
    # 方案一
    # from django.template import loader
    # t = loader.get_template('test_html.html')
    # html = t.render() #将t转换成html字符串
    # return HttpResponse(html)

    # 方案二
    from django.shortcuts import render
    dic = {
        'name':'yh'
    }
    return render(request, 'test_html.html', dic)

def test_html_param(request):



    dic = {}
    dic['int'] = 88
    dic['str'] = 'yh'
    dic['lst'] = ['Tom', 'John', 'Smith']
    dic['dict'] = {'a':9, 'b':6}
    dic['func'] = say_hi
    dic['class_obj'] = Dog()
    dic['script'] = '<script>alert(1111)</script>'

    return render(request, 'test_html_param.html', dic)

def say_hi():
    return 'hahahaha'

class Dog():
    def say(self):
        return 'wangwang'

def test_if_for(request):

    dic = {}
    dic['x'] = 10
    dic['lst'] = ['Tom', 'John', 'Sam']
    return render(request, 'test_if_for.html', dic)

def test_mycal(request):

    if request.method == 'GET':
        return render(request, 'mycal.html')
    elif request.method == 'POST':
        #处理计算
        x = int(request.POST.get('x'))
        y = int(request.POST.get('y'))
        op = request.POST.get('op')

        result = 0
        if op not in ['add', 'sub', 'mul', 'div']:
            return HttpResponse("Your op is wrong")
        elif op == 'add':
            result = x + y
        elif op == 'sub':
            result = x - y
        elif op == 'mul':
            result = x * y
        elif op == 'div':
            result = x / y

        return render(request, 'mycal.html', locals())# 封装当前函数所有变量为一个字典

def base_view(request):

    return render(request, 'base.html')

def music_view(request):

    return render(request, 'music.html')

def sports_view(request):

    return render(request, 'sports.html')

def test_url(request):

    return render(request, 'test_url.html')

def test_url_result(request, age):

    # return HttpResponse('---test url res is ok')

    # 302跳转
    url = reverse('base_index')
    return HttpResponseRedirect(url)