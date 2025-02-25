import time

import redis

pool = redis.ConnectionPool(host='127.0.0.1', db=0, port=6379)
r = redis.Redis(connection_pool=pool)

def double_account(user_id):

    key = 'account_%s'%(user_id)
    with r.pipeline(transaction=True) as pipe:
        while True:
            try:
                pipe.watch(key)
                value = int(r.get(key))
                value *= 2
                print('sleep is start')
                time.sleep(10)
                print('sleep is end')
                pipe.multi()
                pipe.set(key, value)
                pipe.execute()
                break
            except redis.WatchError:
                print('---key changed---')
                continue
    return int(r.get(key))


if __name__ == '__main__':

    print(double_account('wyh'))



# bind 127.0.0.1
# port 26379
# sentinel monitor mymaster 127.0.0.1 6379 2


# from redis.sentinel import Sentinel
# #生成哨兵连接
# sentinel = Sentinel([('127.0.0.1',26379)], socket_timeout=0.1)
# #初始化master连接
# master = sentinel.master_for('mymaster', socket_timeout=0.1, db=1)
# slave = sentinel.slave_for('mymaster',socket_timeout=0.1, db=1)
# #使用redis相关命令
# master.set('mymaster', 'yes')
# print(slave.get('mymaster'))