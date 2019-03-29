import requests
import json
import pymysql
import datetime
from postman_manage.models import Collections
from django.shortcuts import render

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


def get_collection(request):
    url = "https://api.getpostman.com/collections"
    headers = {"X-Api-Key": "a0b4bb86e8f246fdb49212b75e2a8da1"}
    # headers = {"X-Api-Key": "a0b4bb86e8f246fdb49212b75e2a8da1"}
    collections = requests.get(url, headers=headers).json()['collections']
    delete_collections = 'delete from postman_manage_collections'
    write_db(delete_collections)
    for i in range(len(collections)):
        collection_id = collections[i]['id']
        collection_name = collections[i]['name']
        collection_owner = collections[i]['owner']
        collection_uid = collections[i]['uid']
        values = (collection_id, collection_name, collection_owner, collection_uid)
        inster_collections = 'INSERT INTO postman_manage_collections(collection_id,collection_name,collection_owner,collection_uid) values' + str(
            values)
        write_db(inster_collections)

    username = request.session.get('user', '')  # 读取浏览器登录session
    collection_list = Collections.objects.all()  # 读取collection
    return render(request, "collections_manage.html", {"user": username, "collections": collection_list})

# sql = "select xkey from postman_manage_xkey"
# xkeys = read_db(sql)
#
# print(xkeys)
