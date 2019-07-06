
from django.db import models
from django.utils import timezone

from common import error
from common.error import LogicException


class Swiped(models.Model):
    MARKS = (
        ('like', '喜欢'),
        ('dislike', '不喜欢'),
        ('superlike', '超级喜欢')
    )

    uid = models.IntegerField()
    sid = models.IntegerField()
    mark = models.CharField(max_length=16,choices=MARKS)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def is_liked(cls, sid, uid):
        return cls.objects.filter(uid=sid, sid=uid,
                                  mark__in=['like','superlike']).exists()

    @classmethod
    def swipe(cls,uid,sid,mark):
        marks=[m for m,_ in cls.MARKS]
        if mark not in marks:
            raise LogicException(error.SWIPE_ERR)

    class Meta:
        db_table = 'swiped'



class Friend(models.Model):

    uid1=models.IntegerField()
    uid2=models.IntegerField()

    @classmethod
    def make_friends(cls,uid1,uid2):
        uid1,uid2=(uid1,uid2) if uid1<=uid2 else (uid2,uid1)
        cls.objects.create(uid1=uid1,uid2=uid2)



    class Meta:
        db_table='friends'

