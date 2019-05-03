import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'test_manage.settings'
django.setup()
import json
from django.contrib.auth.decorators import login_required
from postman_manage.models import Envs
import requests
from django.shortcuts import render
from postman_manage.views import write_db
from postman_manage.views import read_db


# envs管理
@login_required
def envs_manage(request):
    username = request.session.get('user', '')  # 读取浏览器登录session
    env_list = Envs.objects.all()  # 读取env
    return render(request, "envs_manage.html", {"user": username, "envs": env_list})


# 根据xkey获取所有的envs
def get_envs(request):
    select_xkey = 'select xkey from postman_manage_xkey'
    xkeys = read_db(select_xkey)
    # print(xkeys)
    # delete_envs = 'delete from postman_manage_envs'
    # write_db(delete_envs)
    for a in range(len(xkeys)):
        xkey = xkeys[a]['xkey']
        url = "https://api.getpostman.com/environments"
        headers = {"X-Api-Key": xkey}
        xkey_owner = read_db("select xkey_owner from postman_manage_xkey where xkey =xkey")[0]["xkey_owner"]
        # headers = {"X-Api-Key": "a0b4bb86e8f246fdb49212b75e2a8da1"}
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            envs = res.json()['environments']
            for i in range(len(envs)):
                env_id = envs[i]['id']
                env_name = envs[i]['name']
                env_owner = xkey_owner
                env_uid = xkey
                values = (env_id, env_name, env_owner, env_uid)
                inster_envs = 'INSERT INTO postman_manage_envs(env_id,env_name,env_owner,env_uid) values' + str(
                    values ) + "ON DUPLICATE KEY UPDATE  env_id=env_id"
                write_db(inster_envs)

    username = request.session.get('user', '')  # 读取浏览器登录session
    env_list = Envs.objects.all()  # 读取env
    return render(request, "envs_manage.html", {"user": username, "envs": env_list})


# 获取单个env
def get_single_env(request):
    # url = "https://api.getpostman.com/envs/8a21f784-14e2-463b-818f-1aa4ecfa8e79"
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
    cid = str(cid)
    print(newfile)
    f = open(newfile, 'w')
    f.close()
    sql = "update postman_manage_envs set env_path =" + "\"" + str(
        file) + "\" where env_id =" + "\"" + cid + "\""
    print(sql)
    write_db(sql)
    return newfile

# env列表搜索
@login_required
def env_search(request):
    username = request.session.get("user", '')
    search_env = request.GET.get("env_name", "")
    envs_list = Envs.objects.filter(env_name__contains=search_env)
    return render(request, 'envs_manage.html', {"user": username, "envs": envs_list})

