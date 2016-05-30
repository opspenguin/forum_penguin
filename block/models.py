#coding:utf-8
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Blocks(models.Model):
    name=models.CharField(u"名称",max_length=30)
    desc=models.CharField(u"描述",max_length=200)
    manager=models.ForeignKey(User,verbose_name="管理员")

    create_timestamp=models.DateField(u"创建时间",auto_now_add=True)
    last_update_timestamp=models.DateField(u"更新时间",auto_now=True)

    class Meta:
        verbose_name="板块"
        verbose_name_plural="板块"