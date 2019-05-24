from django.db import models

# Create your models here.
class Dbs(models.Model):
    name = models.CharField('name', max_length=200)  # 数据库名称
    host = models.CharField('host', max_length=200)  # host
    port = models.CharField('port', max_length=200)  # port
    user = models.CharField('user', max_length=200)  # user
    password = models.CharField('password', max_length=200)  # password
    db = models.CharField('db', max_length=200)  # db
    remark = models.CharField('remark', max_length=200)  # 备注
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间，自动获取当前时间

    class Meta:
        verbose_name = 'Dbs'
        verbose_name_plural = 'Dbs'

    def __str__(self):
        return self.Dbs