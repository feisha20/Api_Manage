from django.db import models

# Create your models here.

class Xkey(models.Model):
    xkey = models.CharField('xkey', max_length=200)  # xkey
    xkey_owner = models.CharField('xkey_owner', max_length=200)  # xkey_owner
    remark = models.CharField('remark', max_length=200)  # remark
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间，自动获取当前时间

    class Meta:
        verbose_name = 'Xkey管理'
        verbose_name_plural = 'Xkey管理'

    def __str__(self):
        return self.xkey