from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
import pymysql
from django.shortcuts import render

# 数据库的链接信息
con = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user='root',
    password='test123456',
    db="apimanage",
    charset="utf8",
)


# 读数据库
def read_db(sql):
    con.ping(reconnect=True)
    cursor = con.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    con.close()
    return result


# 写数据库
def write_db(sql):
    con.ping(reconnect=True)
    cursor = con.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql)
    con.commit()
    cursor.close()
    con.close()


# 登录
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


# 首页
def home(request):
    return render(request, "home.html")


# 登出
def logout(request):
    auth.logout(request)
    return render(request, 'login.html')
