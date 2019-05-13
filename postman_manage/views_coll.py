# -*- coding: UTF-8 -*-
import django
import os
import subprocess
import psutil

os.environ['DJANGO_SETTINGS_MODULE'] = 'test_manage.settings'
django.setup()
import json
from django.contrib.auth.decorators import login_required
import requests
from postman_manage import models
from django.shortcuts import render
from postman_manage.models import Collections


# collections管理
@login_required
def collections_manage(request):
    username = request.session.get('user', '')  # 读取浏览器登录session
    collection_list = Collections.objects.all().filter(status=1)  # 读取collection
    xkey_list = models.Xkey.objects.all()
    return render(request, "collections_manage.html", {"user": username, "collections": collection_list, "xkeys": xkey_list})


# 根据xkey获取所有的collections
def get_collections(request):
    if request.method == 'POST':
        xkey = request.POST.get('xkey')
        xkey_owner = models.Xkey.objects.filter(xkey=xkey).values_list("xkey_owner", flat=True)[0]
        url = "https://api.getpostman.com/collections"
        headers = {"X-Api-Key": xkey}
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            collections = res.json()['collections']
            for i in range(len(collections)):
                collection_ids = models.Collections.objects.values_list("collection_id", flat=True)
                if collections[i]['id'] not in collection_ids:
                    models.Collections.objects.create(
                        collection_id=collections[i]['id'],
                        collection_name=collections[i]['name'],
                        collection_owner=xkey_owner,
                        collection_uid=xkey,
                        status=1,

                    )
    username = request.session.get('user', '')  # 读取浏览器登录session
    collection_list = Collections.objects.all().filter(status=1)  # 读取collection
    xkey_list = models.Xkey.objects.all()
    return render(request, "collections_manage.html", {"user": username, "collections": collection_list, "xkeys": xkey_list})


# 获取单个collection
def get_single_collection(request):
    # url = "https://api.getpostman.com/collections/8a21f784-14e2-463b-818f-1aa4ecfa8e79"
    cid = request.GET.get('cid')
    xkey = request.GET.get('xkey')
    url = "https://api.getpostman.com/collections/" + cid
    headers = {"X-Api-Key": xkey}
    collection = requests.get(url, headers=headers).json()
    collection_name = collection["collection"]['info']['name']
    collection_file = create_collection_json_file(collection_name, cid)
    with open(collection_file, 'w', encoding='utf-8') as json_file:
        json.dump(collection, json_file, ensure_ascii=False)
    username = request.session.get('user', '')  # 读取浏览器登录session
    collection_list = Collections.objects.all().filter(status=1)  # 读取collection
    xkey_list = models.Xkey.objects.all()
    return render(request, "collections_manage.html", {"user": username, "collections": collection_list, "xkeys": xkey_list})


# 创建json文件
def create_collection_json_file(filename, cid):
    path = os.path.dirname(__file__) + "/collections/"
    suffix = ".json"
    file = "col-" + filename + suffix
    newfile = path + file
    f = open(newfile, 'w')
    models.Collections.objects.filter(collection_id=cid).update(collection_path=file)
    return newfile


# collection列表搜索
@login_required
def collection_search(request):
    username = request.session.get("user", '')
    search_collection = request.GET.get("collection_name", "")
    collections_list = Collections.objects.filter(collection_name__contains=search_collection).filter(status=1)
    xkey_list = models.Xkey.objects.all()
    return render(request, "collections_manage.html",
                  {"user": username, "collections": collections_list, "xkeys": xkey_list})


# 修改collection
@login_required
def eidt_collection(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = models.Collections.objects.filter(id=nid).first()
        return render(request, 'edit_collection.html', {'obj': obj})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        remark = request.POST.get('remark')
        status = request.POST.get('status')
        models.Collections.objects.filter(id=nid).update(
            remark=remark,
            status=status
        )
        collection_list = Collections.objects.all().filter(status=1)  # 读取collection
        xkey_list = models.Xkey.objects.all()
        return render(request, "collections_manage.html", {"collections": collection_list, "xkeys": xkey_list})


# 删除collection
@login_required
def del_collection(request):
    nid = request.GET.get('nid')
    models.Collections.objects.filter(id=nid).delete()
    collection_list = Collections.objects.all().filter(status=1)  # 读取collection
    xkey_list = models.Xkey.objects.all()
    return render(request, "collections_manage.html", {"collections": collection_list, "xkeys": xkey_list})


# Runcollection
@login_required
def get_collection_detail(request):
    nid = request.GET.get('nid')
    uid = request.GET.get('uid')
    obj = models.Collections.objects.filter(id=nid).first()
    obj2 = models.Envs.objects.filter(env_uid=uid).all().exclude(env_path='')
    return render(request, 'run_collection.html', {'obj': obj, 'obj2': obj2})


@login_required
def run_collection(request):
    env_file = request.POST.get('env_path')
    print("env_file:" + env_file)
    cid = request.POST.get('cid')
    col_file = request.POST.get('collection_path')
    col_file_name = request.POST.get('collection_name')
    report_file = col_file_name + ".html"
    # f = subprocess.call('cd ../collections & newman run col-demo2.json -r html --reporter-html-export', shell=True)
    collections_path = os.path.dirname(__file__) + "/collections/"
    report_path = os.path.dirname(__file__) + "/report/"
    report_template_path = os.path.dirname(__file__) + "/collections/templates/"
    report_template = "--ignore-redirects --reporters cli,html --reporter-html-template" + report_template_path + "template-default-colored.hbs"
    if env_file != "":
        run_sh = "newman run " + collections_path + col_file + " -g " + collections_path + "globals.json" + " -e " + collections_path + str(
            env_file) + " -r html --reporter-html-export " + report_path + report_file + " " + report_template
    else:
        run_sh = "newman run " + collections_path + col_file + " -r html --reporter-html-export " + report_path + report_file + " " + report_template
    print(run_sh)
    p = subprocess.Popen(run_sh, shell=True)
    pid = p.pid
    models.Collections.objects.filter(id=cid).update(run_pid=pid)
    collection_list = Collections.objects.all().filter(status=1)
    xkey_list = models.Xkey.objects.all()
    f = p.wait()
    if f == 0:
        models.Collections.objects.filter(id=cid).update(run_status=1)
        return render(request, "collections_manage.html", {"collections": collection_list, "xkeys": xkey_list})
    else:
        models.Collections.objects.filter(id=cid).update(run_status=0)
        return render(request, "collections_manage.html", {"collections": collection_list, "xkeys": xkey_list})


@login_required
def stop_collection(request):
    nid = request.GET.get('nid')
    obj = models.Collections.objects.filter(id=nid).first()
    collection_list = Collections.objects.all().filter(status=1)
    pid = obj.run_pid
    children_id = psutil.Process(int(pid)).children()
    children_id = str(children_id).split()[0].split('=')[-1].split(',')[0]
    print("-----------杀死newman进程--------------")
    shell = "kill -9  " + str(children_id)
    print(shell)
    subprocess.Popen(shell)
    return render(request, 'collections_manage.html', {"collections": collection_list, "xkeys": xkey_list})
