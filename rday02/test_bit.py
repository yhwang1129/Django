import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

r.setbit('test', 4, 1)
# print(r.getbit('test', 4))
# print(r.getbit('test', 3))
print(r.bitcount('test'))