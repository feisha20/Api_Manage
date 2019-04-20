# -*- coding: UTF-8 -*-
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
import pymysql

# 数据库信息
database_list = {"base_qa", "business_qa", "capital_qa", "collateral_qa", "product_qa", "risk_qa", "web_qa", 'gel_erp'}
# base_qa = pymysql.connect(host="uat.zpx.server.topideal.work", port=19090, user="base_qa", password="qa@LinEsum.Com", db="base_qa", charset='utf8')
# business_qa = pymysql.connect(host="uat.zpx.server.topideal.work", port=19094, user="business_qa", password="qa@LinEsum.Com", db="business_qa", charset='utf8')
# capital_qa = pymysql.connect(host="uat.zpx.server.topideal.work", port=19093, user="capital_qa", password="qa@LinEsum.Com", db="capital_qa", charset='utf8')
# collateral_qa = pymysql.connect(host="uat.zpx.server.topideal.work", port=19092, user="collateral_qa", password="qa@LinEsum.Com", db="collateral_qa", charset='utf8')
# product_qa = pymysql.connect(host="uat.zpx.server.topideal.work", port=19091, user="product_qa", password="qa@LinEsum.Com", db="product_qa", charset='utf8')
# risk_qa = pymysql.connect(host="uat.zpx.server.topideal.work", port=19096, user="risk_qa", password="qa@LinEsum.Com", db="risk_qa", charset='utf8')
# web_qa = pymysql.connect(host="uat.zpx.server.topideal.work", port=19095, user="web_qa", password="qa@LinEsum.Com", db="web_qa", charset='utf8')


# 连接数据库
def connr(database, sql):
    if database in database_list:
        if database == "base_qa":
            con = pymysql.connect(host="uat.zpx.server.topideal.work", port=19090, user="base_qa", password="qa@LinEsum.Com", db="base_qa", charset='utf8')
        elif database == "business_qa":
            con = pymysql.connect(host="uat.zpx.server.topideal.work", port=19094, user="business_qa", password="qa@LinEsum.Com", db="business_qa", charset='utf8')
        elif database == "capital_qa":
            con = pymysql.connect(host="uat.zpx.server.topideal.work", port=19093, user="capital_qa", password="qa@LinEsum.Com", db="capital_qa", charset='utf8')
        elif database == "collateral_qa":
            con = pymysql.connect(host="uat.zpx.server.topideal.work", port=19092, user="collateral_qa", password="qa@LinEsum.Com", db="collateral_qa", charset='utf8')
        elif database == "product_qa":
            con = pymysql.connect(host="uat.zpx.server.topideal.work", port=19091, user="product_qa", password="qa@LinEsum.Com", db="product_qa", charset='utf8')
        elif database == "risk_qa":
            con = pymysql.connect(host="uat.zpx.server.topideal.work", port=19096, user="risk_qa", password="qa@LinEsum.Com", db="risk_qa", charset='utf8')
        elif database == "web_qa":
            con = pymysql.connect(host="uat.zpx.server.topideal.work", port=19095, user="web_qa", password="qa@LinEsum.Com", db="web_qa", charset='utf8')
        elif database == "gel_erp":
            con = pymysql.connect(host="infra.mysql.topideal.work", port=3306, user="gel_erp", password="FfEKVrbBeyzEyH9IDUiW", db="gel_erp", charset='utf8')
        con.ping(reconnect=True)
        cursor = con.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    else:
        return None

# 连接数据库
def connw(database, sql):
    if database in database_list:
        if database == "base_qa":
            con = pymysql.connect(host="uat.zpx.server.topideal.work", port=19090, user="base_qa", password="qa@LinEsum.Com", db="base_qa", charset='utf8')
        elif database == "business_qa":
            con = pymysql.connect(host="uat.zpx.server.topideal.work", port=19094, user="business_qa", password="qa@LinEsum.Com", db="business_qa", charset='utf8')
        elif database == "capital_qa":
            con = pymysql.connect(host="uat.zpx.server.topideal.work", port=19093, user="capital_qa", password="qa@LinEsum.Com", db="capital_qa", charset='utf8')
        elif database == "collateral_qa":
            con = pymysql.connect(host="uat.zpx.server.topideal.work", port=19092, user="collateral_qa", password="qa@LinEsum.Com", db="collateral_qa", charset='utf8')
        elif database == "product_qa":
            con = pymysql.connect(host="uat.zpx.server.topideal.work", port=19091, user="product_qa", password="qa@LinEsum.Com", db="product_qa", charset='utf8')
        elif database == "risk_qa":
            con = pymysql.connect(host="uat.zpx.server.topideal.work", port=19096, user="risk_qa", password="qa@LinEsum.Com", db="risk_qa", charset='utf8')
        elif database == "web_qa":
            con = pymysql.connect(host="uat.zpx.server.topideal.work", port=19095, user="web_qa", password="qa@LinEsum.Com", db="web_qa", charset='utf8')
        elif database == "gel_erp":
            con = pymysql.connect(host="infra.mysql.topideal.work", port=3306, user="gel_erp", password="FfEKVrbBeyzEyH9IDUiW", db="gel_erp", charset='utf8')
        con.ping(reconnect=True)
        cursor = con.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            cursor.execute(sql)
            con.commit()
        except Exception:
            con.rollback()
            print(Exception)
            return Exception
        finally:
            cursor.close()
            con.close()
    else:
        return None

# 添加测试接口
@csrf_exempt
def sqlr(request):
    sql = request.POST.get('sql', '')
    database = request.POST.get('database', '')
    if sql != "":
        if connr(database, sql) is not None:
            result = connr(database, sql)
            return JsonResponse(result, safe=False)
        else:
            return JsonResponse({"code": 10001, "message": "输入的数据库有误"})
    else:
        return JsonResponse({"code": 10002, "message": "sql语句不能为空"})


# 添加测试接口
@csrf_exempt
def sqlw(request):
    sql = request.POST.get('sql', '')
    database = request.POST.get('database', '')
    if sql != "":
         if connw(database, sql) is None:
            return JsonResponse({"code": 200, "message": "执行成功"})
         else:
             return JsonResponse({"code": 417, "message": "执行失败"})
    elif database != "":
        if connw(database, sql) is None:
            return JsonResponse({"code": 200, "message": "执行完毕"})
        else:
            return JsonResponse({"code": 417, "message": "执行失败"})
    else:
        return JsonResponse({"code": 10002, "message": "sql语句不能为空"})
