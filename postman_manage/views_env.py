import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'test_manage.settings'
django.setup()
import json
from django.contrib.auth.decorators import login_required
from postman_manage.models import Envs
import requests
from django.shortcuts import render
from postman_manage import models


# envs管理
@login_required
def envs_manage(request):
    username = request.session.get('user', '')  # 读取浏览器登录session
    env_list = Envs.objects.all().filter(status=1)   # 读取env
    xkey_list = models.Xkey.objects.all()
    return render(request, "envs_manage.html", {"user": username, "envs": env_list, "xkeys": xkey_list})


# 根据xkey获取所有的envs
def get_envs(request):
    if request.method == 'POST':
        xkey = request.POST.get('xkey')
        xkey_owner = models.Xkey.objects.filter(xkey=xkey).values_list("xkey_owner", flat=True)[0]
        url = "https://api.getpostman.com/environments"
        headers = {"X-Api-Key": xkey}
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            envs = res.json()['environments']
            for i in range(len(envs)):
                env_ids = models.Envs.objects.values_list("env_id", flat=True)
                if envs[i]['id'] not in env_ids:
                    models.Envs.objects.create(
                        env_id=envs[i]['id'],
                        env_name=envs[i]['name'],
                        env_owner=xkey_owner,
                        env_uid=xkey,
                        type=0,
                        status=1,

                    )
    username = request.session.get('user', '')  # 读取浏览器登录session
    env_list = Envs.objects.all().filter(status=1)   # 读取env
    xkey_list = models.Xkey.objects.all()
    return render(request, "envs_manage.html", {"user": username, "envs": env_list, "xkeys": xkey_list})


# 获取单个env
def get_single_env(request):
    cid = request.GET.get('cid')
    xkey = request.GET.get('xkey')
    url = "https://api.getpostman.com/environments/" + cid
    headers = {"X-Api-Key": xkey}
    env = requests.get(url, headers=headers).json()
    env_name = env["environment"]['name']
    env_file = create_env_json_file(env_name, cid)
    with open(env_file, 'w', encoding='utf-8') as json_file:
        json.dump(env, json_file, ensure_ascii=False)
    username = request.session.get('user', '')  # 读取浏览器登录session
    env_list = Envs.objects.all().filter(status=1)   # 读取env
    xkey_list = models.Xkey.objects.all()
    return render(request, "envs_manage.html", {"user": username, "envs": env_list, "xkeys": xkey_list})


# 创建json文件
def create_env_json_file(filename, cid):
    path = os.path.dirname(__file__) + "/collections/"
    suffix = ".json"
    file = "env-" + filename + suffix
    newfile = path + file
    f = open(newfile, 'w')
    f.close()
    models.Envs.objects.filter(env_id=cid).update(env_path=file)
    return newfile


# env列表搜索
@login_required
def env_search(request):
    username = request.session.get("user", '')
    search_env = request.GET.get("env_name", "")
    env_list = Envs.objects.filter(env_name__contains=search_env).filter(status=1)
    xkey_list = models.Xkey.objects.all()
    return render(request, "envs_manage.html", {"user": username, "envs": env_list, "xkeys": xkey_list})


# 删除env
@login_required
def del_env(request):
    nid = request.GET.get('nid')
    models.Envs.objects.filter(id=nid).delete()
    env_list = Envs.objects.all().filter(status=1)
    xkey_list = models.Xkey.objects.all()
    return render(request, "envs_manage.html", {"envs": env_list, "xkeys": xkey_list})


# 修改env
@login_required
def eidt_env(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = models.Envs.objects.filter(id=nid).first()
        return render(request, 'edit_env.html', {'obj': obj})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        status = request.POST.get('status')
        models.Envs.objects.filter(id=nid).update(
            status=status
        )
        env_list = Envs.objects.all().filter(status=1)  # 读取envs
        xkey_list = models.Xkey.objects.all()
        return render(request, "envs_manage.html", {"envs": env_list, "xkeys": xkey_list})


# 手动上传
@login_required
def add_env(request):
    xkey_list = models.Xkey.objects.all()
    if request.method == 'GET':
        return render(request, 'add_env.html', {"xkeys": xkey_list})
    elif request.method == 'POST':
        env_id = request.POST.get('env_id')
        env_name = request.POST.get('env_name')
        type = request.POST.get('type')
        env_owner = request.POST.get('env_owner')
        env_uid = models.Xkey.objects.filter(xkey_owner=env_owner).values_list("xkey",flat=True)[0]
        myFile = request.FILES.get("env_path", None)  # 获取上传的文件，如果没有文件，则默认为None
        path = os.path.dirname(__file__) + "/collections/"
        destination = open(os.path.join(path, myFile.name),
                           'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        models.Envs.objects.create(
            env_id=env_id,
            env_name=env_name,
            type=type,
            env_owner=env_owner,
            env_path=myFile,
            status=1,
            env_uid=env_uid
        )
    env_list = Envs.objects.all().filter(status=1)   # 获取envs
    return render(request, "envs_manage.html", {"envs": env_list})
