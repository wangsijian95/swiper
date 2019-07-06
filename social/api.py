from common import error
from lib.http import render_json
from social import logic
from social.models import Swiped


def recommond(request):
    recm_users=logic.recommend_user()
    users=[s.to_dict() for s in recm_users]
    return render_json(data=users)
def like(request):
    sid=int(request.POST.get('sid'))
    user=request.user
    if logic.like_someone(user.id,sid):
        return render_json()
    else:
        return render_json(code=error.LIKE_ERR)


def dislike(request):
    sid = int(request.POST.get('sid'))
    user = request.user
    Swiped.objects.create(sid=sid,uid=user.id,mark='dislike')


def superlike(request):
    return None


def rewind(request):
    return None


def like_me(request):
    pass

    # logic.liked_me(request,user)






def friends(request):
    pass