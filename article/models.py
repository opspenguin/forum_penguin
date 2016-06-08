#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from block.models import Blocks
# Create your models here.

class Article(models.Model):
    title=models.CharField(u"标题",max_length=30)
    content=models.CharField(u"内容",max_length=10000)
    status = models.IntegerField(u"状态", choices=((0, u"普通"), (-1, u"删除"), (10, u"精华")), default=0)
    owner=models.ForeignKey(User,verbose_name=u"作者")
    block=models.ForeignKey(Blocks,verbose_name=u"板块")

    create_timestamp=models.DateTimeField(u"创建时间",auto_now_add=True)
    last_update_timestamp=models.DateTimeField(u"更新时间",auto_now=True)

    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name=u"文章"
        verbose_name_plural=u"文章"