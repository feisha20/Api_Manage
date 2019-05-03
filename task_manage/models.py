from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    content = models.CharField('content', max_length=200)  # 任务内容
    status = models.CharField('status', max_length=200)  # 状态
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间，自动获取当前时间

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Task'

    def __str__(self):
        return self.Task
