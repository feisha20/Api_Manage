from django.urls import path
from sys_settings import views_dbs

app_name = 'sys_settings'
urlpatterns = [
    path('dbs_manage/', views_dbs.get_dbs),
    path('add_db.html', views_dbs.add_db),
    path('edit_db.html', views_dbs.eidt_db),
    path('del_db.html', views_dbs.del_db),
    path('dbsearch/', views_dbs.db_search),
]