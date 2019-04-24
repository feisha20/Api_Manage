from django.shortcuts import render
from sys_settings import models
from sys_settings.models import Dbs
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.

# DBS管理
@login_required
def get_dbs(request):
    username = request.session.get('user', '')  # 读取浏览器登录session
    dbs_list = Dbs.objects.all()  # 读取db
    return render(request, "dbs_manage.html", {"user": username, "dbs": dbs_list})


# 新增db
@login_required
def add_db(request):
    if request.method == 'GET':
        return render(request, 'add_db.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        host = request.POST.get('host')
        port = request.POST.get('port')
        user = request.POST.get('user')
        password = make_password(request.POST.get('password'), 'pbkdf2_sha256')
        db = request.POST.get('db')
        models.Dbs.objects.create(
            name=name,
            host=host,
            port=port,
            user=user,
            password=password,
            db=db
        )
    db_list = Dbs.objects.all()  # 读取db
    return render(request, "dbs_manage.html", {"dbs": db_list})


# 修改db
@login_required
def eidt_db(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = models.Dbs.objects.filter(id=nid).first()
        return render(request, 'edit_db.html', {'obj': obj})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        name = request.POST.get('name')
        host = request.POST.get('host')
        port = request.POST.get('port')
        user = request.POST.get('user')
        password = request.POST.get('password')
        db = request.POST.get('db')
        models.Dbs.objects.filter(id=nid).update(
            name=name,
            host=host,
            port=port,
            user=user,
            password=password,
            db=db,

        )
        db_list = Dbs.objects.all()  # 读取db
        return render(request, "dbs_manage.html", {"dbs": db_list})


# 删除db
@login_required
def del_db(request):
    nid = request.GET.get('nid')
    models.Dbs.objects.filter(id=nid).delete()
    db_list = Dbs.objects.all()  # 读取db
    return render(request, "dbs_manage.html", {"dbs": db_list})


# db列表搜索
@login_required
def db_search(request):
    username = request.session.get("user", '')
    search_name = request.GET.get("name", "")
    db_list = Dbs.objects.filter(name__contains=search_name)
    return render(request, 'dbs_manage.html', {"user": username, "dbs": db_list})