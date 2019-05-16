from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from task_manage import models
from task_manage.models import Task


# Task管理
@login_required
def tasks(request):
    username = request.session.get('user', '')  # 读取浏览器登录session
    task_list = Task.objects.filter(owner=request.user).exclude(status=4).order_by("-create_time")  # 读取db
    return render(request, "task_manage.html", {"user": username, "tasks": task_list})


# 新增task
@login_required
def add_task(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        models.Task.objects.create(
            content=content,
            status=0,
            owner=request.user
        )
    task_list0 = Task.objects.filter(owner=request.user).filter(status=0).order_by("-create_time")
    task_list1 = Task.objects.filter(owner=request.user).filter(status=1).order_by("-create_time")
    task_list2 = Task.objects.filter(owner=request.user).filter(status=2).order_by("-create_time")
    return render(request, "task_list.html",
                  {"tasks0": task_list0, "tasks1": task_list1, "tasks2": task_list2})


# 任务列表
@login_required
def task_list(request):
    username = request.session.get('user', '')  # 读取浏览器登录session
    task_list0 = Task.objects.filter(owner=request.user).filter(status=0).order_by("-create_time")
    task_list1 = Task.objects.filter(owner=request.user).filter(status=1).order_by("-create_time")
    task_list2 = Task.objects.filter(owner=request.user).filter(status=2).order_by("-create_time")
    return render(request, "task_list.html", {"user": username, "tasks0": task_list0, "tasks1": task_list1, "tasks2": task_list2})


# 修改task to 进行中
@login_required
def to_task1(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        models.Task.objects.filter(id=nid).update(
            status=1,
        )
        task_list0 = Task.objects.filter(owner=request.user).filter(status=0).order_by("-create_time")
        task_list1 = Task.objects.filter(owner=request.user).filter(status=1).order_by("-create_time")
        task_list2 = Task.objects.filter(owner=request.user).filter(status=2).order_by("-create_time")
        return render(request, "task_list.html",
                      {"tasks0": task_list0, "tasks1": task_list1, "tasks2": task_list2})


# 修改task to 完成
@login_required
def to_task2(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        models.Task.objects.filter(id=nid).update(
            status=2,
        )
        task_list0 = Task.objects.filter(owner=request.user).filter(status=0).order_by("-create_time")
        task_list1 = Task.objects.filter(owner=request.user).filter(status=1).order_by("-create_time")
        task_list2 = Task.objects.filter(owner=request.user).filter(status=2).order_by("-create_time")
        return render(request, "task_list.html",
                      {"tasks0": task_list0, "tasks1": task_list1, "tasks2": task_list2})


# 修改task to 新建
@login_required
def to_task0(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        models.Task.objects.filter(id=nid).update(
            status=0,
        )
        task_list0 = Task.objects.filter(owner=request.user).filter(status=0).order_by("-create_time")
        task_list1 = Task.objects.filter(owner=request.user).filter(status=1).order_by("-create_time")
        task_list2 = Task.objects.filter(owner=request.user).filter(status=2).order_by("-create_time")
        return render(request, "task_list.html",
                      {"tasks0": task_list0, "tasks1": task_list1, "tasks2": task_list2})


# 修改task to 完成但不显示在任务列表
@login_required
def to_task3(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        models.Task.objects.filter(id=nid).update(
            status=3,
        )
        task_list0 = Task.objects.filter(owner=request.user).filter(status=0).order_by("-create_time")
        task_list1 = Task.objects.filter(owner=request.user).filter(status=1).order_by("-create_time")
        task_list2 = Task.objects.filter(owner=request.user).filter(status=2).order_by("-create_time")
        return render(request, "task_list.html",
                      {"tasks0": task_list0, "tasks1": task_list1, "tasks2": task_list2})


# 修改task to 作废
@login_required
def to_task4(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        models.Task.objects.filter(id=nid).update(
            status=4,
        )
        task_list0 = Task.objects.filter(owner=request.user).filter(status=0).order_by("-create_time")
        task_list1 = Task.objects.filter(owner=request.user).filter(status=1).order_by("-create_time")
        task_list2 = Task.objects.filter(owner=request.user).filter(status=2).order_by("-create_time")
        return render(request, "task_list.html",
                      {"tasks0": task_list0, "tasks1": task_list1, "tasks2": task_list2})


# 任务列表搜索
@login_required
def task_search(request):
    username = request.session.get("user", '')
    search_content = request.GET.get("content", "")
    task_list = Task.objects.filter(content__contains=search_content).exclude(status=4).order_by("-create_time")
    return render(request, 'task_manage.html', {"user": username, "tasks": task_list})