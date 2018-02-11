from django.db import models


# Create your models here.

class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('姓名', max_length=30, db_column='name')
    email = models.EmailField('邮箱', max_length=50, db_column='email')
    phone = models.CharField('手机号', max_length=11, db_column='phone')
    sex = models.CharField('性别', max_length=1, db_column='sex')
    title = models.CharField('主题', max_length=100, db_column='title')
    content = models.TextField('内容', max_length=500, db_column='content')
    status_val = (('1', u'有效'), ('0', u'无效'))
    status = models.CharField('状态', choices=status_val, max_length=1, db_column='status', default=1)
    createdTime = models.DateTimeField('创建时间', db_column='created_time')
    # blank=True -- 是针对表单的，如果 blank=True，表示你的表单填写该字段的时候可以不填
    # null=True -- null 是针对数据库而言，如果 null=True, 表示数据库的该字段可以为空ss
    updatedTime = models.DateTimeField('更新时间', db_column='updated_time', null=True, blank=True)

    class Meta:
        # 指定表名
        db_table = 'comments'

        verbose_name = '留言'
        verbose_name_plural = '留言'
