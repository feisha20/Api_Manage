import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'Api_Manage.settings'
django.setup()
import json
from django.contrib.auth.decorators import login_required
from postman_manage.models import Collections
import requests
from django.shortcuts import render
from postman_manage.models import Collections
from postman_manage.views import write_db
from postman_manage.views import read_db


# collections管理
@login_required
def collections_manage(request):
    username = request.session.get('user', '')  # 读取浏览器登录session
    collection_list = Collections.objects.all()  # 读取collection
    return render(request, "collections_manage.html", {"user": username, "collections": collection_list})


# 根据xkey获取所有的collections
def get_collections(request):
    select_xkey = 'select xkey from postman_manage_xkey'
    xkeys = read_db(select_xkey)
    # print(xkeys)
    # delete_collections = 'delete from postman_manage_collections'
    # write_db(delete_collections)
    for a in range(len(xkeys)):
        xkey = xkeys[a]['xkey']
        url = "https://api.getpostman.com/collections"
        headers = {"X-Api-Key": xkey}
        # headers = {"X-Api-Key": "a0b4bb86e8f246fdb49212b75e2a8da1"}
        xkey_owner = read_db("select xkey_owner from postman_manage_xkey where xkey =xkey")[0]["xkey_owner"]
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            collections = res.json()['collections']
            for i in range(len(collections)):
                collection_id = collections[i]['id']
                collection_name = collections[i]['name']
                collection_owner = xkey_owner
                collection_uid = xkey
                values = (collection_id, collection_name, collection_owner, collection_uid)
                inster_collections = 'INSERT INTO postman_manage_collections(collection_id,collection_name,collection_owner,collection_uid) values' + str(
                    values ) + "ON DUPLICATE KEY UPDATE  collection_id=collection_id"
                write_db(inster_collections)

    username = request.session.get('user', '')  # 读取浏览器登录session
    collection_list = Collections.objects.all()  # 读取collection
    return render(request, "collections_manage.html", {"user": username, "collections": collection_list})


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
    collection_list = Collections.objects.all()  # 读取collection
    return render(request, "collections_manage.html", {"user": username, "collections": collection_list})


# 创建json文件
def create_collection_json_file(filename, cid):
    path = "F:\\Api_manage\\collections\\"
    suffix = ".json"
    file = "col-" + filename + suffix
    newfile = path + file
    cid = str(cid)
    print(newfile)
    f = open(newfile, 'w')
    f.close()
    sql = "update postman_manage_collections set collection_path =" + "\"" + str(
        file) + "\" where collection_id =" + "\"" + cid + "\""
    print(sql)
    write_db(sql)
    return newfile

# collection列表搜索
@login_required
def collection_search(request):
    username = request.session.get("user", '')
    search_collection = request.GET.get("collection_name", "")
    collections_list = Collections.objects.filter(collection_name__contains=search_collection)
    return render(request, 'collections_manage.html', {"user": username, "collections": collections_list})

#
# xkey_owner = read_db("select xkey_owner from postman_manage_xkey where xkey =xkey")[0]["xkey_owner"]
# print(xkey_owner)