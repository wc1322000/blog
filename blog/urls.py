"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from myblog.views import IndexView, ArichiveView, TagView, TagDetailView, BlogDetailView
from django.urls import re_path

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', IndexView.as_view(), name='index'),  # 首页的url
    re_path(r'^archive/$', ArichiveView.as_view(), name='archive'),
    re_path(r'^tags/$', TagView.as_view(), name='tags'),
    re_path(r'^tags/(?P<tag_name>\w+)$', TagDetailView.as_view(), name='tag_name'),
    re_path(r'^blog/(?P<blog_id>\d+)$', BlogDetailView.as_view(), name='blog_id'),
]

