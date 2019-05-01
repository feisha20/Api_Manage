from django.shortcuts import render
from project_manage import models
from project_manage.models import Projects, ProjectVersion
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.

# projects管理
@login_required
def get_projects(request):
    username = request.session.get('user', '')  # 读取浏览器登录session
    projects_list = Projects.objects.all()  # 读取project
    return render(request, "projects_manage.html", {"user": username, "projects": projects_list})


# 新增project
@login_required
def add_project(request):
    if request.method == 'GET':
        return render(request, 'add_project.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        remark = request.POST.get('remark')
        models.Projects.objects.create(
            name=name,
            remark=remark,
        )
    project_list = Projects.objects.all()  # 读取project
    return render(request, "projects_manage.html", {"projects": project_list})


# 修改project
@login_required
def eidt_project(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = models.Projects.objects.filter(id=nid).first()
        return render(request, 'edit_project.html', {'obj': obj})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        name = request.POST.get('name')
        remark = request.POST.get('remark')
        models.Projects.objects.filter(id=nid).update(
            name=name,
            remark=remark,

        )
        project_list = Projects.objects.all()  # 读取project
        return render(request, "projects_manage.html", {"projects": project_list})


# 删除project
@login_required
def del_project(request):
    nid = request.GET.get('nid')
    models.Projects.objects.filter(id=nid).delete()
    project_list = Projects.objects.all()  # 读取project
    return render(request, "projects_manage.html", {"projects": project_list})


# project列表搜索
@login_required
def project_search(request):
    username = request.session.get("user", '')
    search_name = request.GET.get("name", "")
    project_list = Projects.objects.filter(name__contains=search_name)
    return render(request, 'projects_manage.html', {"user": username, "projects": project_list})
