from django.urls import path
from .views import signup_view, login_view, logout_view
from .views import signup_api, login_api

app_name = 'accounts'

urlpatterns = [
    #path('signup/', signup_view, name = 'signup'),
    #path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('signup/', signup_api, name='signup'),
    path('login/', login_api, name='login'),


]