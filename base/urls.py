from django.urls import path
from base import views

app_name = 'base'
urlpatterns = [
    path('edit_user_info.html', views.eidt_user_info),

]