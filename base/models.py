from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User_info(models.Model):
    sex = models.BooleanField('性别',default=0) # 性别
    remark = models.CharField('remark', max_length=200)  # 备注
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间，自动获取当前时间

    class Meta:
        verbose_name = 'User_info'
        verbose_name_plural = 'User_info'

    def __str__(self):
        return self.User_info
