"""test_manage URL Configuration

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
from django.urls import path
from . import views
from django.views.static import serve
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  url(r'^$', views.login),
                  path('login/', views.login),
                  path('release_log/', views.project_log),
                  path('base/login.html', views.logout),
                  path('home/', views.home),
                  path('home/index_v2.html', views.index),
                  path('logout/', views.logout),
                  path('index2/', views.index2),
                  path('file_manage/', views.file_manage),
                  url(r'^postman_manage/', include('postman_manage.urls', namespace="postman_manage")),
                  url(r'^base/', include('base.urls', namespace="base")),
                  url('^report/(?P<path>.*)$', serve, {'document_root': settings.REPORT_ROOT}),
                  url(r'^project/', include('project_manage.urls', namespace="project_manage")),
                  url(r'^web_auto/', include('web_auto.urls', namespace="web_auto")),
                  url(r'^task/', include('task_manage.urls', namespace="task_manage")),
                  url(r'^sys_settings/', include('sys_settings.urls', namespace="sys_settings")),
                  url(r'^open_api/', include('open_api.urls', namespace="open_api")),
                  url(r'^favicon.ico$',RedirectView.as_view(url=r'static/img/favicon.ico')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
