import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

r.hset('test', mapping={'key1': 'value1', 'key2': 'value2'})
print(r.hgetall('test'))