from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index_view(request):

    # return HttpResponse("这是新闻频道")
    return render(request, 'news/index.html')# 放在news文件夹下保证不会找错html