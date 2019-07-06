'''
业务返回码
'''
ok=0

#用户系统
PHONE_NUM_ERR=1001  #手机号格式错误
VERIFY_CODE_ERR=1003  #验证码错误
LOGIN_REQUIRED=1004    #未登录
AVATAR_UPLOAD_ERR=1005    #上传头像失败

class LogicException(Exception):
    def __init__(self, code):
        self.code = code





# 社交系统
LIKE_ERR = 2001  # 喜欢失败