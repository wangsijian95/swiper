from django.urls import path, include

from user import api


urlpatterns = [
    path('verify-code',api.verify_phone),
    path('user-login',api.login),
    path('get-profile',api.get_profile),
    path('set-profile',api.set_profile),
    path('upload-avatar',api.upload_avatar),
]