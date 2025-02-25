from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import re

class MyMW(MiddlewareMixin):

    #请求到达路由之前调用
    def process_request(self, request):

        print('MyMW process_request do ---')
        #没有return默认返回None
    def process_view(self, request, callback, callback_args, callback_kwargs):

        print('MyMW process_view do ---')

    #服务器响应前也就是客户端传过来后先调用
    def process_response(self, request, response):

        print('MyMW process_response do ---')
        return response#这个要求必须返回response

class MyMW2(MiddlewareMixin):

    #请求到达路由之前调用
    def process_request(self, request):

        print('MyMW2 process_request do ---')
        #没有return默认返回None
    def process_view(self, request, callback, callback_args, callback_kwargs):

        print('MyMW2 process_view do ---')

    #服务器响应前也就是客户端传过来后先调用
    def process_response(self, request, response):

        print('MyMW2 process_response do ---')
        return response#这个要求必须返回response


# 中间件实现请求拦截
class VisitLimit(MiddlewareMixin):
    # 存储每个IP地址的访问次数
    visit_times = {}

    def process_request(self, request):
        # 获取访问者的IP地址和请求的路由
        ip_address = request.META['REMOTE_ADDR']
        path_url = request.path_info

        # 仅对以'/test'开头的路由进行限制
        if not re.match('^/test', path_url):
            return  # 如果不匹配，直接返回

        # 获取当前IP的访问次数，默认为0
        times = self.visit_times.get(ip_address, 0)
        print('ip', ip_address, '已经访问', times)

        # 更新访问次数
        self.visit_times[ip_address] = times + 1

        # 如果访问次数小于5，则允许访问
        if times < 5:
            return

        # 如果访问次数达到限制，返回禁止访问的响应
        return HttpResponse('您已经访问过' + str(times) + '次，被禁止访问')
