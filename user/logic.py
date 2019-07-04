from django.core.cache import cache

from common import config
from common.utils import gen_random_code
from lib import sms

# 发送验证码
def send_verify_code(phone_num):
    code=gen_random_code(length=6)
    ret=sms.send(phone_num,code)

    if ret:
        cache.set(config.VERIFY_CODE_CACHE_PREFIX % phone_num,code,60*60)
        # print('-----0',cache.get(config.VERIFY_CODE_CACHE_PREFIX % phone_num))
    return ret
