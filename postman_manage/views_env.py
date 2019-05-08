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
    env_list = Envs.objects.all()  # 读取env
    return render(request, "envs_manage.html", {"user": username, "envs": env_list})


# 根据xkey获取所有的envs
def get_envs(request):
    xkeys = models.Xkey.objects.values_list("xkey", flat=True)
    for a in range(len(xkeys)):
        xkey = xkeys[a]
        url = "https://api.getpostman.com/environments"
        headers = {"X-Api-Key": xkey}
        xkey_owner = models.Xkey.objects.values_list("xkey_owner", flat=True)[a]
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

                    )
    username = request.session.get('user', '')  # 读取浏览器登录session
    env_list = Envs.objects.all()  # 读取env
    return render(request, "envs_manage.html", {"user": username, "envs": env_list})


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
    env_list = Envs.objects.all()  # 读取env
    return render(request, "envs_manage.html", {"user": username, "envs": env_list})


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
    envs_list = Envs.objects.filter(env_name__contains=search_env)
    return render(request, 'envs_manage.html', {"user": username, "envs": envs_list})
