import random
import re

PHONE_PATTERN=re.compile(r'^1[3-9]\d{9}$')


def is_Phone_num(phone_num):
    return True if PHONE_PATTERN.match(phone_num) else False


def gen_random_code(length=4):
    if length<=0:
        length=1
    code=random.randrange(10**(length-1),10**length)
    return str(code)

