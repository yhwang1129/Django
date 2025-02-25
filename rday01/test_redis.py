import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')

# #基础命令
# key_list = r.keys('*')
# print(key_list)
# #[b'uuname', b'uname', b'l1', b'trill:username']
# print(r.type('l1'))
#
#
# ###list###
# r.lpush('lyl1', 'a', 'v', 'w', 'z')
# print(r.lrange('lyl1', 0, -1))
# r.linsert('lyl1', 'before', 'v', 'g')
# print(r.lrange('lyl1', 0, -1))

##string
r.set('puname', 'wang', ex=30)
print(r.get('puname'))