from django.urls import path
from project_manage import views

app_name = 'project_manage'
urlpatterns = [
    path('projects_manage/', views.get_projects),
    path('add_project.html', views.add_project),
    path('edit_project.html', views.eidt_project),
    path('del_project.html', views.del_project),
    path('projectsearch/', views.project_search),
    path('projectversion_manage/', views.get_projectversion),
    path('add_projectversion.html', views.add_projectversion),
    path('edit_projectversion.html', views.eidt_projectversion),
    path('del_projectversion.html', views.del_projectversion),
    path('projectversionsearch/', views.projectversion_search),
]