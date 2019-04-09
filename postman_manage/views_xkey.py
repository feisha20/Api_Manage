from postman_manage.models import Xkey
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from postman_manage import models


# Xkey管理
@login_required
def get_xkey(request):
    username = request.session.get('user', '')  # 读取浏览器登录session
    xkey_list = Xkey.objects.all()  # 读取xkey
    return render(request, "xkey_manage.html", {"user": username, "xkeys": xkey_list})


# 新增xkey
@login_required
def add_xkey(request):
    if request.method == 'GET':
        return render(request, 'add_xkey.html')
    elif request.method == 'POST':
        xkey = request.POST.get('xkey')
        xkey_owner = request.POST.get('xkey_owner')
        remark = request.POST.get('remark')
        models.Xkey.objects.create(
            xkey=xkey,
            xkey_owner=xkey_owner,
            remark=remark

        )
    xkey_list = Xkey.objects.all()  # 读取xkey
    return render(request, "xkey_manage.html", {"xkeys": xkey_list})


# 修改xkey
@login_required
def eidt_xkey(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = models.Xkey.objects.filter(id=nid).first()
        return render(request, 'edit_xkey.html', {'obj': obj})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        xkey = request.POST.get('xkey')
        xkey_owner = request.POST.get('xkey_owner')
        remark = request.POST.get('remark')
        models.Xkey.objects.filter(id=nid).update(
            xkey=xkey,
            xkey_owner=xkey_owner,
            remark=remark

        )
        xkey_list = Xkey.objects.all()  # 读取xkey
        return render(request, "xkey_manage.html", {"xkeys": xkey_list})


# 删除xkey
@login_required
def del_xkey(request):
    nid = request.GET.get('nid')
    models.Xkey.objects.filter(id=nid).delete()
    xkey_list = Xkey.objects.all()  # 读取xkey
    return render(request, "xkey_manage.html", {"xkeys": xkey_list})


# xkey列表搜索
@login_required
def xkey_search(request):
    username = request.session.get("user", '')
    search_owner = request.GET.get("xkey_owner", "")
    xkey_list = Xkey.objects.filter(xkey_owner__contains=search_owner)
    return render(request, 'xkey_manage.html', {"user": username, "xkeys": xkey_list})
