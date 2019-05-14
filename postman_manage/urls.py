from django.urls import path
from postman_manage import views_coll
from postman_manage import views_xkey
from postman_manage import views_env

app_name = 'postman_manage'
urlpatterns = [
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
    path('del_env.html', views_env.del_env),
    path('edit_env.html', views_env.eidt_env),
    path('add_env.html', views_env.add_env),
    path('get_single_env.html', views_env.get_single_env),
    path('edit_collection.html', views_coll.eidt_collection),
    path('del_collection.html', views_coll.del_collection),
    path('run_collection.html', views_coll.get_collection_detail),
    path('run_collection/', views_coll.run_collection),
    path('stop_collection.html/', views_coll.stop_collection),
]