from django.urls import path, re_path
from .views import *

app_name = 'articles'

urlpatterns = [
    path('',articles_list,name='list'),
    path('create', create_article, name='create'),
    path('<slug:slug>', article_detail,name='detail'),
]