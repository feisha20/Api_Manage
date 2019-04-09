# Generated by Django 2.1.7 on 2019-03-27 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postman_manage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_id', models.CharField(max_length=200, verbose_name='collection_id')),
                ('collection_name', models.CharField(max_length=200, verbose_name='collection_name')),
                ('collection_owner', models.CharField(max_length=200, verbose_name='collection_owner')),
                ('collection_uid', models.CharField(max_length=200, verbose_name='collection_uid')),
                ('collection_path', models.CharField(max_length=200, verbose_name='collection_path')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': 'Collections管理',
                'verbose_name_plural': 'Collections管理',
            },
        ),
    ]