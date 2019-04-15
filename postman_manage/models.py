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


class Collections(models.Model):
    collection_id = models.CharField('collection_id', max_length=200)  # collection_id
    collection_name = models.CharField('collection_name', max_length=200)  # collection_name
    collection_owner = models.CharField('collection_owner', max_length=200)  # collection_owner
    collection_uid = models.CharField('collection_uid', max_length=200)  # collection_uid
    collection_path = models.CharField('collection_path', max_length=200)  # collection_path
    run_pid = models.CharField('run_pid',max_length=20) # run_pid
    status = models.BooleanField('是否有效') # status
    run_status = models.BooleanField('运行结果')  # run_status
    remark = models.CharField('remark', max_length=200)  # remark
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间，自动获取当前时间

    class Meta:
        verbose_name = 'Collections管理'
        verbose_name_plural = 'Collections管理'

    def __str__(self):
        return self.Collections


class Envs(models.Model):
    env_id = models.CharField('env_id', max_length=200)  # env_id
    env_name = models.CharField('env_name', max_length=200)  # env_name
    env_owner = models.CharField('env_owner', max_length=200)  # env_owner
    env_uid = models.CharField('env_uid', max_length=200)  # env_uid
    env_path = models.CharField('env_path', max_length=200)  # env_path
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间，自动获取当前时间

    class Meta:
        verbose_name = 'Env管理'
        verbose_name_plural = 'Env管理'

    def __str__(self):
        return self.Envs