# 导入 json 模块，用于处理 JSON 数据
import json
# 导入 redis 模块，用于与 Redis 数据库进行交互
import redis

# 创建 Redis 连接对象
# host: Redis 服务器的 IP 地址
# port: Redis 服务器的端口（默认是 6379）
# db: 使用的 Redis 数据库索引（默认是 0）
# password: 连接 Redis 时所需的密码（如果 Redis 未设置密码，可以省略此参数）
r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')

# 创建一个字典，包含要发送的任务信息
json_obj = {
    'task': 'send_mail',  # 任务类型
    'send_mail': 'aaa',   # 邮件内容或相关信息
    'from': 'bbbb',       # 发件人地址
    'to': 'cccc'          # 收件人地址
}

# 将字典转换为 JSON 格式的字符串
json_str = json.dumps(json_obj)

# 将 JSON 字符串推入 Redis 列表 'pyl2' 的左侧
r.lpush('pyl2', json_str)
