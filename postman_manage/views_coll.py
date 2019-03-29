import django
import os
import json
os.environ['DJANGO_SETTINGS_MODULE'] = 'Api_Manage.settings'
django.setup()
import requests
import pymysql
from django.shortcuts import render
from postman_manage.models import Collections

con = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user='root',
    password='test123456',
    db="apimanage",
    charset="utf8",
)


def read_db(sql):
    cursor = con.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def write_db(sql):
    con.ping(reconnect=True)
    cursor = con.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql)
    con.commit()
    cursor.close()
    con.close()


def get_collections(request):
    select_xkey = 'select xkey from postman_manage_xkey'
    xkeys = read_db(select_xkey)
    print(xkeys)
    delete_collections = 'delete from postman_manage_collections'
    write_db(delete_collections)
    for a in range(len(xkeys)):
        xkey = xkeys[a]['xkey']
        url = "https://api.getpostman.com/collections"
        headers = {"X-Api-Key": xkey}
        # headers = {"X-Api-Key": "a0b4bb86e8f246fdb49212b75e2a8da1"}
        collections = requests.get(url, headers=headers).json()['collections']
        for i in range(len(collections)):
            collection_id = collections[i]['id']
            collection_name = collections[i]['name']
            collection_owner = collections[i]['owner']
            collection_uid = xkey
            values = (collection_id, collection_name, collection_owner, collection_uid)
            inster_collections = 'INSERT INTO postman_manage_collections(collection_id,collection_name,collection_owner,collection_uid) values' + str(
                values)
            write_db(inster_collections)

    username = request.session.get('user', '')  # 读取浏览器登录session
    collection_list = Collections.objects.all()  # 读取collection
    return render(request, "collections_manage.html", {"user": username, "collections": collection_list})


def get_single_collection(request):
    url = "https://api.getpostman.com/collections/8a21f784-14e2-463b-818f-1aa4ecfa8e79"
    headers = {"X-Api-Key": "a0b4bb86e8f246fdb49212b75e2a8da1"}
    collection = requests.get(url, headers=headers).json()
    collection_name = collection["collection"]['info']['name']
    collection_file= create_collection_json_file(collection_name)
    with open(collection_file, 'w', encoding='utf-8') as json_file:
        json.dump(collection, json_file, ensure_ascii=False)
    username = request.session.get('user', '')  # 读取浏览器登录session
    collection_list = Collections.objects.all()  # 读取collection
    return render(request, "collections_manage.html", {"user": username, "collections": collection_list})


def create_collection_json_file(filename):
    path = "F:\\Api_manage\\collections\\"
    suffix = ".json"
    file = filename + suffix
    newfile = path + file
    print(newfile)
    f = open(newfile, 'w')
    f.close()
    sql = "update postman_manage_collections set collection_path =" + "\"" + str(file) + "\""
    print(sql)
    write_db(sql)
    return newfile
