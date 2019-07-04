from django.core.cache import cache
from django.http import JsonResponse

from common import error, config
from common.utils import is_Phone_num
from lib import http
from lib.http import render_json
from user import logic
from user.forms import ProfileForm
from user.models import User


def verify_phone(request):
    '''
    验证手机号
    :return:
    '''
    phone_num=request.POST.get('phone_num')

    result=is_Phone_num(phone_num.strip())

    if result:
        # 生成随即验证码
        # 发送随即验证码
        logic.send_verify_code(phone_num)
        return http.render_json()
    return http.render_json(code=error.PHONE_NUM_ERR)

def login(request):
    phone_num = request.POST.get('phone_num','')
    code=request.POST.get('code','')

    phonenum=phone_num.strip()
    code=code.strip()
    print('--2',code)
    cached_code=cache.get(config.VERIFY_CODE_CACHE_PREFIX % phone_num)
    print('------1',cached_code)
    if code != cached_code:
        return http.render_json(code=error.VERIFY_CODE_ERR)

    user,created=User.objects.get_or_create(phonenum=phonenum)
    request.session['uid']=user.id
    return http.render_json(data=user.to_dict())


def get_profile(request):
   profile=request.user.profile
   return render_json(data=profile.to_dict(exclude=['vibration','only_matche','auto_play']))

def set_profile(request):
    user=request.user
    forms=ProfileForm(request.POST)
    if forms.is_valid():
        profile=forms.save(commit=False)
        profile.id=user.id
        profile.save()
        return render_json()
    else:
        return render_json(data=forms.errors)



def upload_avatar(request):
    pass