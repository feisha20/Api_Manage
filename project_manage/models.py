from django.db import models


# Create your models here.
class Projects(models.Model):
    name = models.CharField('name', max_length=200)  # 产品名称
    remark = models.CharField('remark', max_length=200)  # 备注
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间，自动获取当前时间

    class Meta:
        verbose_name = 'Projects'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.Projects


class ProjectVersion(models.Model):
    project_name = models.CharField('project_name', max_length=200)  # 产品名称
    version_no = models.CharField('version_no', max_length=200)  # 版本号
    summary = models.CharField('summary', max_length=600)  # 版本概要
    detail = models.CharField('detail', max_length=200)  # 版本详细内容
    publish_date = models.DateTimeField('publish_date', max_length=200)  # 发布日期
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间，自动获取当前时间

    class Meta:
        verbose_name = 'ProjectVersion'
        verbose_name_plural = 'ProjectVersion'

    def __str__(self):
        return self.ProjectVersion