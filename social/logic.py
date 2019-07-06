import datetime

from common import config
from social.models import Swiped
from user.models import User


def recommend_user(user):
    '''
    筛选符合user.profile条件的用户
    过滤掉已经被划过的用户
    :param user:
    :return:
    '''
    today=datetime.date.today()
    max_year=today.year-user.profile.min_dating_age
    min_year=today.year-user.profile.max_dating_age

    swiped_user=Swiped.objects.filter(id=user.id).only('sid')
    swiped_user_list=[s.uid for s in swiped_user]

    users=User.objects.filter(
        sex=user.profile.dating_sex,
        location=user.profile.location,
        birth_day__gte=min_year,
        birth_day__lte=max_year,
    ).exclude(id__in=swiped_user_list)[:20]
    return users


def like_someone(uid,sid):
    if not User.objects.filter(id=sid).exists():
        return False
    Swiped.objects.create(uid=uid,sid=sid,mark='like')

    if Swiped.is_liked(sid,uid):
        print('yue')
    return 1


def superlike_someone(uid,sid):
    if not User.objects.filter(id=sid).exists():
        return False
    Swiped.objects.create(uid=uid,sid=sid,mark='superlike')

    if Swiped.is_liked(sid,uid):
        print('yue')
    return 1


def rewind(user):
    '''

    :param user:
    :return:
    '''
    key=config.REWIND_CACHE_PREFIX%(user.id)


def liked_me(user):
    swipe_list=Swiped.objects.filter(sid=user.id,
                                     mark__in=['like','superlike'])
    # 过滤掉已经价位好友的用户
    liked_me_uid_list=[s.uid for s in swipe_list]



    return None