from django.db import models


# Create your models here.
class AutoProjects(models.Model):
    name = models.CharField('name', max_length=200)  # 项目名称
    job_name = models.CharField('job_name', max_length=200)  # JOB名称
    remark = models.CharField('remark', max_length=200)  # 备注
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间，自动获取当前时间

    class Meta:
        verbose_name = 'AutoProjects'
        verbose_name_plural = 'AutoProjects'

    def __str__(self):
        return self.AutoProjects


# 测试用例
class AutoCase(models.Model):
    project = models.CharField('project', max_length=200)  # 所属项目
    title = models.CharField('title', max_length=200)  # 用例名称
    case_path = models.CharField('case_path', max_length=200)  # 用例路径
    summary = models.CharField('summary', max_length=200)  # 用例说明
    mark = models.CharField('mark', max_length=200)  # 标识
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间，自动获取当前时间

    class Meta:
        verbose_name = 'AutoCase'
        verbose_name_plural = 'AutoCase'

    def __str__(self):
        return self.AutoCase


# 测试集
class TestSuit(models.Model):
    project = models.CharField('project', max_length=200)  # 所属项目
    name = models.CharField('name', max_length=200)  # 测试集名称
    case_ids = models.CharField('case_ids', max_length=600)  # 用例名称
    shell = models.CharField('shell', max_length=1000)  # 用例路径
    build_job = models.CharField("build_job", max_length=200)  # jenkins Job
    job_url = models.CharField("job_url", max_length=200)  # jenkins job_url
    result = models.CharField('result', max_length=200)  # 用例说明
    run_time = models.DateTimeField('运行时间')  # 运行时间
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间，自动获取当前时间

    class Meta:
        verbose_name = 'TestSuit'
        verbose_name_plural = 'TestSuit'

    def __str__(self):
        return self.TestSuit
