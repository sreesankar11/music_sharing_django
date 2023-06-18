from django.urls import path
from musicapp import views
from .views import homepage, profile_view, Upload
from .views import register_view, login_view, logout_view


app_name = 'musicapp'

from django.urls import path
from .views import (
    login_view,
    register_view,
    homepage,
    Upload,
    profile_view,
    logout_view,
)

urlpatterns = [
    path('accounts/login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('', homepage, name='homepage'),
    path('upload/', Upload, name='upload'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
    
]