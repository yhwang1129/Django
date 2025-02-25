from django.http import HttpResponse

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