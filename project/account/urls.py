from django.urls import path, re_path
from .views import *

app_name = 'account'

urlpatterns = [
    path('signup',signup_view,name='signup'),
    path('login', login_view,name='login'),
    path('logout', logout_view,name='logout'),
]