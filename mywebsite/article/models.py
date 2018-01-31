# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

'''
    文章app的模块有如下几个：
    (1) 文章分类 ：Java ，Python 等
    (2) 文章 
'''

'''
    文章分类表：article_category包含如下字段
    (1) id 主键
    (2) category_code 分类code
    (3) category_name 分类名称
    (4) status 状态 (1：表示有效,0表示无效)
    (5) created_time 创建时间
    (6) updated_time 更新时间
'''


class ArticleCategory(models.Model):
    id = models.IntegerField('主键', primary_key=True, db_column='id')
    categoryCode = models.CharField('分类编码', max_length=20, db_column='category_code')
    categoryName = models.CharField('分类名称', max_length=30, db_column='category_name')
    status = models.CharField('状态', max_length=1, db_column='status')
    createdTime = models.DateTimeField('创建时间', db_column='created_time')
    updatedTime = models.DateTimeField('更新时间', db_column='updated_time', null=True, blank=True)

    # 后台admin中显示，在一对多选择的时候会显示名称，否则显示ArticleCategory object
    def __str__(self):
        return self.categoryName

    class Meta:
        # 指定表名
        db_table = 'article_category'


'''
    文章表：article包含如下字段
    (1) id 主键
    (2) article_title 文章主题
    (3) article_category_id 文章分类(外键)
    (4) article_content 文章内容
    (5) status 状态 (1：表示有效,0表示无效)
    (6) created_time 创建时间
    (7) updated_time 更新时间
'''


class Article(models.Model):
    id = models.IntegerField('主键', primary_key=True, db_column='id')
    articleTitle = models.CharField('主题', max_length=30, db_column='article_title')
    articleContent = models.CharField('内容', max_length=500, db_column='article_content')
    # 一对多(一个Article对应多个ArticleCategory) on_delete=models.CASCADE 级联删除，也就是当删除主表的数据时候从表中的数据也随着一起删除
    articleCategory = models.ForeignKey('ArticleCategory', db_column='article_category_id', on_delete=models.CASCADE,
                                        blank=True, null=True)
    status = models.CharField('状态', max_length=1, db_column='status')
    createdTime = models.DateTimeField('创建时间', db_column='created_time')
    updatedTime = models.DateTimeField('更新时间', db_column='updated_time', null=True, blank=True)

    class Meta:
        # 指定表名
        db_table = 'article'
