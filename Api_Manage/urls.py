"""Api_Manage URL Configuration

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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('home/', views.home),
    path('logout/', views.logout),
    path('get_xkey/', views_xkey.get_xkey),
    path('add_xkey.html', views_xkey.add_xkey),
    path('edit_xkey.html', views_xkey.eidt_xkey),
    path('del_xkey.html', views_xkey.del_xkey),
    path('collections_manage/', views_coll.collections_manage),
    path('get_collections/', views_coll.get_collections),
    path('get_single_collection.html', views_coll.get_single_collection),
    path('apisearch/', views_xkey.xkey_search),
    path('collection_search/', views_coll.collection_search),
]
