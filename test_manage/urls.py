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
from postman_manage import views
from postman_manage import views_coll
from postman_manage import views_xkey
from postman_manage import views_env
from django.views.static import serve
from django.conf import settings
from django.conf.urls import url, include
from sys_settings import views_dbs
from open_api import views_open
from django.conf.urls.static import static
from project_manage import views_project

urlpatterns = [
                  path('admin/', admin.site.urls),
                  url(r'^$', views.login),
                  path('login/', views.login),
                  path('home/', views.home),
                  path('home/index_v2.html', views.index),
                  path('logout/', views.logout),
                  path('get_xkey/', views_xkey.get_xkey),
                  path('add_xkey.html', views_xkey.add_xkey),
                  path('edit_xkey.html', views_xkey.eidt_xkey),
                  path('del_xkey.html', views_xkey.del_xkey),
                  path('collections_manage/', views_coll.collections_manage),
                  path('get_collections/', views_coll.get_collections),
                  path('get_single_collection.html', views_coll.get_single_collection),
                  path('xkeysearch/', views_xkey.xkey_search),
                  path('collection_search/', views_coll.collection_search),
                  path('envs_manage/', views_env.envs_manage),
                  path('get_envs/', views_env.get_envs),
                  path('get_singel_env.html/', views_env.get_single_env),
                  path('env_search/', views_env.env_search),
                  path('get_single_env.html', views_env.get_single_env),
                  path('edit_collection.html', views_coll.eidt_collection),
                  path('del_collection.html', views_coll.del_collection),
                  path('run_collection.html', views_coll.get_collection_detail),
                  path('run_collection/', views_coll.run_collection),
                  path('stop_collection.html/', views_coll.stop_collection),
                  url('^report/(?P<path>.*)$', serve, {'document_root': settings.REPORT_ROOT}),
                  path('dbs_manage/', views_dbs.get_dbs),
                  path('projects_manage/', views_project.get_projects),
                  path('add_project.html', views_project.add_project),
                  path('edit_project.html', views_project.eidt_project),
                  path('del_project.html', views_project.del_project),
                  path('projectsearch/', views_project.project_search),
                  path('projectversion_manage/', views_project.get_projectversion),
                  path('add_projectversion.html', views_project.add_projectversion),
                  path('add_db.html', views_dbs.add_db),
                  path('edit_db.html', views_dbs.eidt_db),
                  path('del_db.html', views_dbs.del_db),
                  path('dbsearch/', views_dbs.db_search),
                  path('file_manage/', views.file_manage),
                  path('task_manage/', views.task_manage),
                  path('index2/', views.index2),
                  url(r'^open_api/', include('open_api.urls', namespace="open_api")),
                  path('open_api/sqlr/', views_open.sqlr),
                  path('open_api/sqlw/', views_open.sqlw),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
