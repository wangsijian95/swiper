from django.urls import path

from social import api

urlpatterns=[
    path('recommond',api.recommond),
    path('like',api.like),
    path('dislike',api.dislike),
    path('superlike',api.superlike),
    path('rewind',api.rewind),
    path('like_me',api.like_me),
    ]