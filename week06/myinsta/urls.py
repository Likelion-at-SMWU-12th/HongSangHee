"""
URL configuration for myinsta project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from posts.views import url_view, url_parameter_view,function_view, class_view
from posts.views import index
from posts.views import calculator
from django.conf.urls.static import static
from django.conf import settings
from posts.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts', PostModelViewSet)

urlpatterns = [ 
    path('', include(router.urls)),
    path('calculator/', calculator),
    path('admin/', admin.site.urls),
    path('url/', url_view),
    path('url/<str:username>/', url_parameter_view),
    path('fbv/',function_view),
    path('cbv/',class_view.as_view()),
    #path('', index, name='index'),
    #path('posts/', include('posts.urls', namespace='posts')),
    #path('posts/', PostListCreateView.as_view()),
    #path('posts/<int:pk>/', PostRetrieveUpdateView.as_view()),
    path('accounts/', include('accounts.urls', namespace='accounts')),

    #로그인
    path('login/', login_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
