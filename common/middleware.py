from django.utils.deprecation import MiddlewareMixin

from common import error
from common.error import LogicException
from lib.http import render_json
from user.models import User


class AuthMiddleware(MiddlewareMixin):
    WHITE_LIST=[
        '/api/user/verify-code',
        '/api/user/user-login'
    ]
    def process_request(self,request):
        if request.path in self.WHITE_LIST:
            return
        uid=request.session.get('uid')
        if uid is None:
            return render_json(code=error.LOGIN_REQUIRED)
        request.user=User.objects.get(id=uid)


class LogicExceptionMiddlewar(MiddlewareMixin):

    def process_exception(self,request,exception):
        if isinstance(exception,LogicException):
            return render_json(code=exception.code)
