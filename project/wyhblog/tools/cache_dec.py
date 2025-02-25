from django.core.cache import cache

from .logging_dec import get_user_by_request

def cache_set(expire):
    def _cache_set(func):
        def wrapper(request, *args, **kwargs):
            #区分场景 - 只做列表页
            if 't_id' in request.GET:
                #当前请求是获取文章详情页
                return func(request, *args, **kwargs)
            #生成出正确的cache key [访客访问 和 博主访问]
            visitor_user = get_user_by_request(request)
            visitor_username = None
            if visitor_user:
                visitor_username = visitor_user.username
            author_username = kwargs.get('author_id', None)
            print('visitor is %s' % (visitor_username))
            print('author is %s' % (author_username))
            full_path = request.get_full_path()
            if visitor_username == author_username:
                cache_key = 'topics_cache_self_%s'%(full_path)
            else:
                cache_key = 'topics_cache_%s'%(full_path)
            print('cache key is %s' % (cache_key))
            #---判断是否有缓存，有缓存直接返回
            res = cache.get(cache_key)
            if res:
                print('---cache in---')
                return res

            #执行视图
            res = func(request, *args, **kwargs)
            #存储换成 cache对象/set/get
            cache.set(cache_key, res, expire)
            #返回响应
            return  res
        return wrapper
    return _cache_set