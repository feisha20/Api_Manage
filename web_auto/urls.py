from django.urls import path
from web_auto import views

app_name = 'web_auto'
urlpatterns = [
    path('autoprojects_manage/', views.get_autoprojects),
    path('add_autoproject.html', views.add_autoproject),
    path('edit_autoproject.html', views.eidt_autoproject),
    path('del_autoproject.html', views.del_autoproject),
    path('autocases_manage/', views.get_autopcases),
    path('add_case.html', views.add_case),
    path('edit_case.html', views.eidt_case),
    path('del_case.html', views.del_case),
    path('testsuits/', views.get_testsuits),
    path('add_testsuit.html', views.add_testsuit),
    path('edit_testsuit.html', views.eidt_testsuit),
    path('del_testsuit.html', views.del_testsuit),
    path('run_test.html', views.run_test),
    path('get_result.html', views.get_result),
]