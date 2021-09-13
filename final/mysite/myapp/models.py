from django.db import models

# Create your models here.
class DataList(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    视频链接 = models.TextField(blank=True, null=True)
    视频名称 = models.TextField(blank=True, null=True)
    简介 = models.TextField(blank=True, null=True)
    封面照片 = models.TextField(blank=True, null=True)
    播放量 = models.TextField(blank=True, null=True)
    弹幕数 = models.TextField(blank=True, null=True)
    评论数 = models.TextField(blank=True, null=True)
    上传日期 = models.TextField(blank=True, null=True)
    点赞数 = models.TextField(blank=True, null=True)
    收藏数 = models.TextField(blank=True, null=True)
    香蕉数 = models.TextField(blank=True, null=True)
    up主名称 = models.TextField(db_column='UP主名称', blank=True, null=True)  # Field name made lowercase.
    up主id = models.TextField(db_column='UP主ID', blank=True, null=True)  # Field name made lowercase.
    up主头像 = models.TextField(db_column='UP主头像', blank=True, null=True)  # Field name made lowercase.
    up主介绍 = models.TextField(db_column='UP主介绍', blank=True, null=True)  # Field name made lowercase.
    up主关注人数 = models.TextField(db_column='UP主关注人数', blank=True, null=True)  # Field name made lowercase.
    评论1 = models.TextField(blank=True, null=True)
    评论2 = models.TextField(blank=True, null=True)
    评论3 = models.TextField(blank=True, null=True)
    评论4 = models.TextField(blank=True, null=True)
    评论5 = models.TextField(blank=True, null=True)
    评论6 = models.TextField(blank=True, null=True)
    评论7 = models.TextField(blank=True, null=True)
    评论8 = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'data_list'