from django.conf.urls import url

from . import views
from . import regist_views
from . import search_views

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^registInput$', regist_views.index, name='index'),
url(r'^regist$', regist_views.create, name='create'),
url(r'^searchInput$', search_views.index, name='index'),
]