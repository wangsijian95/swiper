import os
import time
from urllib.parse import urljoin

from django.conf import settings
from django.core.cache import cache

from common import config
from common.utils import gen_random_code
from lib import sms, qiniuyun


# 发送验证码
from worker import celery_app


def send_verify_code(phone_num):
    code=gen_random_code(length=6)
    ret=sms.send(phone_num,code)

    if ret:
        cache.set(config.VERIFY_CODE_CACHE_PREFIX % phone_num,code,60*60)
        # print('-----0',cache.get(config.VERIFY_CODE_CACHE_PREFIX % phone_num))
    return ret


def upload_file(filename,f):
    filepath = os.path.join(settings.MEDIA_ROOT, filename)

    with open(filepath, 'wb+') as output:
        for chunk in f.chunks():
            output.write(chunk)
    return filepath

def upload_qiniuyun(filename,filepath):
    ret, info=qiniuyun.upload(filename,filepath)
    if info.status_code==200:
        return True
    else:
        return False


@celery_app.task
def async_upload_avatar(user,avatar):
    # 上传文件至本地服务器
    filename = 'avatar-%s-%d' % (user.id, int(time.time()))

    filepath =upload_file(filename, avatar)
    # 再将本地服务器文件直接上传七牛云
    ret = upload_qiniuyun(filename, filepath)

    if ret:
        user.avatar = urljoin(config.QN_HOST, filename)
        user.save()
    else:
        return ret