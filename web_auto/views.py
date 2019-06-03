import os
import django
import datetime
import xml.dom.minidom as xmldom
import time

os.environ['DJANGO_SETTINGS_MODULE'] = 'test_manage.settings'
django.setup()
from django.shortcuts import render
from web_auto import models
from web_auto.models import AutoProjects, AutoCase, TestSuit
from django.contrib.auth.decorators import login_required
import pymysql
from test_manage.settings import DATABASES2, JENKINS_SETTINGS
import subprocess
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.

# autoprojects管理
@login_required
def get_autoprojects(request):
    username = request.session.get('user', '')  # 读取浏览器登录session
    autoprojects_list = AutoProjects.objects.all()  # 读取project
    return render(request, "autoprojects_manage.html", {"user": username, "autoprojects": autoprojects_list})


# 新增Auto_project
@login_required
def add_autoproject(request):
    if request.method == 'GET':
        return render(request, 'add_autoproject.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        job_name = request.POST.get('job_name')
        remark = request.POST.get('remark')
        models.AutoProjects.objects.create(
            name=name,
            job_name=job_name,
            remark=remark,
        )
    project_list = AutoProjects.objects.all()  # 读取project
    return render(request, "autoprojects_manage.html", {"autoprojects": project_list})


# 修改autoproject
@login_required
def eidt_autoproject(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = models.AutoProjects.objects.filter(id=nid).first()
        return render(request, 'edit_autoproject.html', {'obj': obj})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        name = request.POST.get('name')
        job_name = request.POST.get('job_name')
        remark = request.POST.get('remark')
        models.AutoProjects.objects.filter(id=nid).update(
            name=name,
            job_name=job_name,
            remark=remark,

        )
        autoprojects_list = AutoProjects.objects.all()  # 读取project
        return render(request, "autoprojects_manage.html", {"autoprojects": autoprojects_list})


# 删除project
@login_required
def del_autoproject(request):
    nid = request.GET.get('nid')
    models.AutoProjects.objects.filter(id=nid).delete()
    autoprojects_list = AutoProjects.objects.all()  # 读取project
    return render(request, "autoprojects_manage.html", {"autoprojects": autoprojects_list})


# autopcases管理
@login_required
def get_autopcases(request):
    username = request.session.get('user', '')  # 读取浏览器登录session
    autocases_list = AutoCase.objects.all()  # 读取caselist
    return render(request, "autocases_manage.html", {"user": username, "autocases": autocases_list})


# 新增AutoCase
@login_required
def add_case(request):
    if request.method == 'GET':
        autoprojects_list = AutoProjects.objects.all()
        return render(request, 'add_case.html', {"autoprojects": autoprojects_list})
    elif request.method == 'POST':
        project = request.POST.get('project')
        title = request.POST.get('title')
        summary = request.POST.get('summary')
        case_path = request.POST.get('case_path')
        mark = request.POST.get('mark')
        models.AutoCase.objects.create(
            project=project,
            title=title,
            summary=summary,
            case_path=case_path,
            mark=mark
        )
    autocases_list = AutoCase.objects.all()  # 读取project
    return render(request, "autocases_manage.html", {"autocases": autocases_list})


# 修改case
@login_required
def eidt_case(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = models.AutoCase.objects.filter(id=nid).first()
        project_obj = models.AutoProjects.objects.all()
        return render(request, 'edit_case.html', {'obj': obj, 'autoprojects': project_obj})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        project = request.POST.get('project')
        title = request.POST.get('title')
        case_path = request.POST.get('case_path')
        mark = request.POST.get('mark')
        summary = request.POST.get('summary')
        models.AutoCase.objects.filter(id=nid).update(
            project=project,
            title=title,
            case_path=case_path,
            mark=mark,
            summary=summary,
        )
        cases_list = AutoCase.objects.all()  # 读取case
        return render(request, "autocases_manage.html", {"autocases": cases_list})


# 删除case
@login_required
def del_case(request):
    nid = request.GET.get('nid')
    models.AutoCase.objects.filter(id=nid).delete()
    cases_list = AutoCase.objects.all()  # 读取case
    return render(request, "autocases_manage.html", {"autocases": cases_list})


# testsuit管理
@login_required
def get_testsuits(request):
    username = request.session.get('user', '')  # 读取浏览器登录session
    testsuits_list = TestSuit.objects.all()  # 读取project
    return render(request, "testsuits.html", {"user": username, "testsuits": testsuits_list})


# 新增testsuit
@login_required
def add_testsuit(request):
    if request.method == 'GET':
        autoprojects_list = AutoProjects.objects.all()
        cases_list = AutoCase.objects.all()  # 读取case
        return render(request, 'add_testsuit.html', {"autoprojects": autoprojects_list, "autocases": cases_list})
    elif request.method == 'POST':
        project = request.POST.get('project')
        name = request.POST.get('name')
        shell = request.POST.get('shell')
        models.TestSuit.objects.create(
            project=project,
            name=name,
            shell=shell,
        )
    testsuits_list = TestSuit.objects.all()  # 读取project
    return render(request, "testsuits.html", {"testsuits": testsuits_list})


# 修改testsuit
@login_required
def eidt_testsuit(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = models.TestSuit.objects.filter(id=nid).first()
        project_obj = models.AutoProjects.objects.all()
        cases_list = AutoCase.objects.all()  # 读取case
        return render(request, 'edit_testsuit.html', {'obj': obj, 'autoprojects': project_obj, "autocases": cases_list})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        project = request.POST.get('project')
        name = request.POST.get('name')
        shell = request.POST.get('shell')
        models.TestSuit.objects.filter(id=nid).update(
            project=project,
            name=name,
            shell=shell,
        )
        testsuits_list = TestSuit.objects.all()  # 读取case
        return render(request, "testsuits.html", {"testsuits": testsuits_list})


# 删除testsuit
@login_required
def del_testsuit(request):
    nid = request.GET.get('nid')
    models.TestSuit.objects.filter(id=nid).delete()
    testsuits_list = TestSuit.objects.all()  # 读取case
    return render(request, "testsuits.html", {"testsuits": testsuits_list})


# webauto数据库的链接信息
db = DATABASES2
con = pymysql.connect(
    host=db["default"]["HOST"],
    port=int(db["default"]["PORT"]),
    user=db["default"]["USER"],
    password=db["default"]["PASSWORD"],
    db=db["default"]["NAME"],
    charset="utf8",
)


# 写数据库
def write_db(sql):
    con.ping(reconnect=True)
    cursor = con.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql)
    con.commit()
    cursor.close()
    con.close()


# 执行测试
def run_test(request):
    nid = request.GET.get('nid')
    shell = models.TestSuit.objects.filter(id=nid).values_list("shell", flat=True)[0]
    run_shell = "python3 /usr/local/python3/lib/python3.6/site-packages/pytest.py -v -s " + shell + " --html=./report/report.html"
    project = models.TestSuit.objects.filter(id=nid).values_list("project", flat=True)[0]
    jobname = models.AutoProjects.objects.filter(name=project).values_list("job_name", flat=True)[0]
    sql = "update run_shell set shell='" + str(run_shell) + "' where id=1"
    write_db(sql)
    jenkins_url = JENKINS_SETTINGS["URL"]
    user = JENKINS_SETTINGS['USER']
    password = JENKINS_SETTINGS['PASSWORD']
    jenkins_cli_jar_path = os.path.dirname(__file__) + "/jenkins_cli/"
    to_jenkins = "java -jar " + jenkins_cli_jar_path + "jenkins-cli.jar -s " + jenkins_url + " -auth " + user + ":" + password + " build " + jobname
    # print(to_jenkins)
    subprocess.Popen(to_jenkins, shell=True)
    models.TestSuit.objects.filter(id=nid).update(
        result="running",
        run_time=datetime.datetime.now()
    )
    testsuits_list = TestSuit.objects.all()  # 读取project
    return render(request, "testsuits.html", {"testsuits": testsuits_list})


def get_result(request):
    nid = request.GET.get('nid')
    project = models.TestSuit.objects.filter(id=nid).values_list("project", flat=True)[0]
    jobname = models.AutoProjects.objects.filter(name=project).values_list("job_name", flat=True)[0]
    jenkins_url = JENKINS_SETTINGS["URL"]
    user = JENKINS_SETTINGS['USER']
    password = JENKINS_SETTINGS['PASSWORD']
    if os.path.exists("./web_auto/build.xml"):
        os.remove("./web_auto/build.xml")
    shell = "curl " + jenkins_url + "job/" + jobname + "/lastBuild/api/xml --user " + user + ":" + password + " >./web_auto/build.xml"
    # print(shell)
    subprocess.Popen(shell, shell=True)
    time.sleep(2)
    domobj = xmldom.parse("./web_auto/build.xml")
    elementobj = domobj.documentElement
    subElementObj = elementobj.getElementsByTagName("building")
    is_running = subElementObj[0].firstChild.data
    if is_running == "true":
        testsuits_list = TestSuit.objects.all()  # 读取project
        return render(request, "testsuits.html", {"testsuits": testsuits_list})
    else:
        subElementObj2 = elementobj.getElementsByTagName("result")
        result = subElementObj2[0].firstChild.data
        models.TestSuit.objects.filter(id=nid).update(
            result=result,
        )
        testsuits_list = TestSuit.objects.all()  # 读取project
        return render(request, "testsuits.html", {"testsuits": testsuits_list})
