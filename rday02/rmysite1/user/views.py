from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import redis

from user.models import User

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

# Create your views here.
def user_detail(request, user_id):
    #/user/detail/1
    cache_key = "user:%s" % (user_id)
    #优先查缓存
    if r.exists(cache_key):
        data = r.hgetall(cache_key)
        #{b'username':b'xxx', b'desc':b'xxx'}
        new_data = {k.decode():v.decode() for k, v in data.items()}
        name = new_data['name']
        desc = new_data['desc']
        html = 'cache username is %s ; desc is %s' % (name, desc)
        return HttpResponse(html)

    #无缓存记录
    try:
        user = User.objects.get(id=user_id)
    except Exception as e:
        print('---get user error is %s'%(e))
        return HttpResponse('---no user---')

    name = user.name
    desc = user.desc
    #更新缓存
    r.hset(cache_key, mapping={'name':name, 'desc':desc})
    r.expire(cache_key, 60)
    html = 'mysql username is %s ; desc is %s' % (name, desc)
    return HttpResponse(html)

def user_update(request):

    if request.method == 'GET':
        return render(request, 'user_update.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')

        try:
            user = User.objects.get(name=name)
        except Exception as e:
            print('---get user error is %s'%(e))
            return HttpResponse('---no user---')

        user.desc = desc
        user.save()

        #删除缓存
        cache_key = "user:%s" % (user.id)
        r.delete(cache_key)
        return HttpResponseRedirect('/user/detail/%s' % (user.id))