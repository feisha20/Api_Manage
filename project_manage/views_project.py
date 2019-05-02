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


# projectversion管理
@login_required
def get_projectversion(request):
    username = request.session.get('user', '')  # 读取浏览器登录session
    projectversion_list = ProjectVersion.objects.all().order_by("-publish_date")  # 读取project
    return render(request, "projectversion_manage.html", {"user": username, "projectversions": projectversion_list})


# projectversion详情
@login_required
def get_projectversion_detail(request):
    nid = request.GET.get('nid')
    Pid = request.GET.get('pid')
    obj = models.ProjectVersion.objects.filter(id=nid).first()
    obj2 = models.Projects.objects.filter(id=Pid).all()
    return render(request, 'run_collection.html', {'obj': obj, 'obj2': obj2})


# 新增project
@login_required
def add_projectversion(request):
    if request.method == 'GET':
        project_list = Projects.objects.all()
        return render(request, 'add_projectversion.html', {"projects":project_list})
    elif request.method == 'POST':
        project_name = request.POST.get('project_name')
        version_no = request.POST.get('version_no')
        summary = request.POST.get('summary')
        detail = request.POST.get('detail')
        publish_date = request.POST.get('publish_date')
        models.ProjectVersion.objects.create(
            project_name=project_name,
            version_no=version_no,
            summary=summary,
            detail=detail,
            publish_date=publish_date,
        )
    projectversion_list = ProjectVersion.objects.all().order_by("-publish_date")  # 读取projectversion
    return render(request, "projectversion_manage.html", {"projectversions": projectversion_list})


# 修改projectversion
@login_required
def eidt_projectversion(request):
    if request.method == 'GET':
        vid = request.GET.get('vid')
        obj = models.ProjectVersion.objects.filter(id=vid).first()
        project_obj = models.Projects.objects.all()
        return render(request, 'edit_projectversion.html', {'obj': obj, 'project_obj':project_obj})
    elif request.method == 'POST':
        vid = request.GET.get('vid')
        project_name = request.POST.get('project_name')
        version_no = request.POST.get('version_no')
        summary = request.POST.get('summary')
        detail = request.POST.get('detail')
        publish_date = request.POST.get('publish_date')
        models.ProjectVersion.objects.filter(id=vid).update(
            project_name=project_name,
            version_no=version_no,
            summary=summary,
            detail=detail,
            publish_date=publish_date,

        )
        projectversions_list = ProjectVersion.objects.all().order_by("-publish_date")  # 读取projectversion
        return render(request, "projectversion_manage.html", {"projectversions": projectversions_list})


# 删除projectversion
@login_required
def del_projectversion(request):
    vid = request.GET.get('vid')
    models.ProjectVersion.objects.filter(id=vid).delete()
    projectversions_list = ProjectVersion.objects.all().order_by("-publish_date")  # 读取projectversion
    return render(request, "projectversion_manage.html", {"projectversions": projectversions_list})


# projectversion列表搜索
@login_required
def projectversion_search(request):
    username = request.session.get("user", '')
    search_name = request.GET.get("project_name", '')
    projectversions_list = ProjectVersion.objects.filter(project_name__contains=search_name).order_by("-publish_date")
    return render(request, 'projectversion_manage.html', {"user": username, "projectversions": projectversions_list})