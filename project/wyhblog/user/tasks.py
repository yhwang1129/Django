from django.conf import settings
from wyhblog.celery import app
from tools.sms import YunTongxin

@app.task
def send_sms_c(phone, code):

    config = settings.SMS_CONFIG

    yun = YunTongxin(**config)
    res = yun.run(phone, code)
    print(res)