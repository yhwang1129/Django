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

# 进入一个无限循环，持续处理任务
while True:
    # 从 Redis 列表 'pyl2' 中阻塞式地弹出一个任务
    # 如果 10 秒内没有任务到来，则返回 None
    task = r.blpop('pyl2', 10)

    # 打印弹出的任务（可能是 None）
    print(task)

    # 如果成功获取到任务
    if task:
        # 将任务的 JSON 字符串解析为 Python 字典
        json_data = json.loads(task[1])

        # 在这里执行具体的任务逻辑
        # 例如，发送邮件、处理数据等
        # 你可以使用 json_data['from'], json_data['to'] 等字段进行操作
    else:
        # 如果没有获取到任务，则打印信息
        print('---no task---')
