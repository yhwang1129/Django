import csv
import time

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

@cache_page(15)
def test_cache(request):

    t = time.time()

    return HttpResponse('t is %s'%(t))

def test_mw(request):
    print('--- test_mw view in ---')
    return HttpResponse('-- test_mw ---')

def test_csrf(request):

    if request.method == 'GET':
        return render(request, 'test_csrf.html')
    elif request.method == 'POST':
        return HttpResponse('--- test post is ok ---')

def test_page(request):

    #/test_page/4
    #/test_page?page=1
    page_num = request.GET.get('page', 1)
    all_data = ['a', 'b', 'c', 'd', 'e']
    #初始化paginator
    paginator = Paginator(all_data, 2)
    #初始化 具体页码的page
    c_page = paginator.page(int(page_num))
    return render(request, 'test_page.html', locals())

def test_csv(request):
    # 创建一个HTTP响应对象，设置内容类型为CSV
    response = HttpResponse(content_type='text/csv')
    # 设置响应头，使浏览器将文件作为附件下载
    response['Content-Disposition'] = 'attachment; filename="test.csv"'
    # 定义要写入CSV文件的数据
    all_data = ['a', 'b', 'c', 'd']
    # 创建CSV写入器
    writer = csv.writer(response)
    # 将数据写入CSV文件的第一行
    writer.writerow(all_data)
    # 返回响应对象
    return response

def make_page_csv(request):

    page_num = request.GET.get('page', 1)
    all_data = ['a', 'b', 'c', 'd', 'e']
    paginator = Paginator(all_data, 2)
    c_page = paginator.page(int(page_num))

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="page-%s.csv"'%(page_num)
    writer = csv.writer(response)
    for b in c_page:
        writer.writerow([b])
    return response

#day08
def test_upload(request):

    if request.method == 'GET':
        return render(request, 'test_upload.html')
    if request.method == 'POST':
        return HttpResponse('---上传文件成功---')