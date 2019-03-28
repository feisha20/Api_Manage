from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from postman_manage.models import Xkey
from postman_manage import models
from postman_manage.models import Collections
import requests
import json


# Create your views here.

def login(request):
    if request.POST:
        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['user'] = username
            response = HttpResponseRedirect('/home/')
            return response
        else:
            return render(request, 'login.html', {'error': 'username or password error'})
    return render(request, 'login.html')


def home(request):
    return render(request, "home.html")


def logout(request):
    auth.logout(request)
    return render(request, 'login.html')


# Xkey管理
@login_required
def xkey_manage(request):
    username = request.session.get('user', '')  # 读取浏览器登录session
    xkey_list = Xkey.objects.all()  # 读取xkey
    return render(request, "xkey_manage.html", {"user": username, "xkeys": xkey_list})


# 保存xkey
@login_required
def save_xkey(request):
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
def update_xkey(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = models.Xkey.objects.filter(id=nid).first()
        return render(request, 'xkey_manage.html', {'obj': obj})
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


# collections管理
@login_required
def collections_manage(request):
    username = request.session.get('user', '')  # 读取浏览器登录session
    collection_list = Collections.objects.all()  # 读取collection
    return render(request, "collections_manage.html", {"user": username, "collections": collection_list})


# 获取collections
def get_all_collection():
    url = "https://api.getpostman.com/collections/8a21f784-14e2-463b-818f-1aa4ecfa8e79"
    headers = {"X-Api-Key": "a0b4bb86e8f246fdb49212b75e2a8da1"}
    res = requests.get(url, headers=headers)
    model = res.json()
    with open("./collections/123.json", 'w', encoding='utf-8') as json_file:
        json.dump(model, json_file, ensure_ascii=False)
