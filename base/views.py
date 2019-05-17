from django.shortcuts import render
from base import models
from base.models import User_info
from django.contrib.auth.decorators import login_required
from project_manage.models import ProjectVersion
from django.contrib.auth.models import User


@login_required
def eidt_user_info(request):
    if request.method == 'POST':
        user_id = request.user.id
        remark = request.POST.get('remark')
        sex = request.POST.get('sex')
        models.User_info.objects.filter(owner=user_id).update(
            remark=remark,
            sex=sex,
        )
        username = request.session.get('user', '')
        user_info = User_info.objects.filter(owner=request.user)
        user = User.objects.filter(username=username)
        projectversion_list = ProjectVersion.objects.all().order_by("-publish_date")  # 读取project
        return render(request, "index_v2.html",
                      {"user": username, "projectversions": projectversion_list, 'user': user, 'user_info': user_info})

@login_required()
def add_user_info(request):

    owner_ids = models.User_info.objects.values_list("owner", flat=True)
    if request.user not in owner_ids:
        models.User_info.objects.create(
            sex=0,
            remark="",
            owner_id=request.user
        )
    return True