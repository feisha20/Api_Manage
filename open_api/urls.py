from django.conf.urls import url
from open_api import views_open

app_name = 'open_api'
urlpatterns = [
    # test_api interface:
    # ex: /oepn_api/sql/
    url(r'sqlr', views_open.sqlr, name='sql'),
    url(r'sqlw', views_open.sqlw, name='sql'),
]