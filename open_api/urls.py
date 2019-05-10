from django.conf.urls import url
from django.urls import path
from open_api import views

app_name = 'open_api'
urlpatterns = [
    # test_api interface:
    # ex: /oepn_api/sql/
    url(r'sqlr', views.sqlr, name='sqlr'),
    url(r'sqlw', views.sqlw, name='sqlw'),
    path('openapi_manage.html/', views.openapi_list),
]