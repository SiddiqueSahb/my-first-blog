from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]


"""
    ^ for the beginning of the text
    $ for the end of the text
    \d for a digit
    + to indicate that the previous item should be repeated at least once
    () to capture part of the pattern
    post/ just means that after the beginning
"""
