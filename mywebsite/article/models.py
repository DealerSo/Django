# -*- coding: utf-8 -*-
from django.db import models
import json
from datetime import date
from datetime import datetime

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
    # id = models.IntegerField('主键', primary_key=True, db_column='id')
    id = models.AutoField(primary_key=True)
    categoryCode = models.CharField('分类编码', max_length=20, db_column='category_code')
    categoryName = models.CharField('分类名称', max_length=30, db_column='category_name')
    # 设定值让status进行选择，默认为default=1 表示有效(类似于select功能)
    status_val = (('1', u'有效'), ('0', u'无效'))
    status = models.CharField('状态', choices=status_val, max_length=1, db_column='status', default=1)
    createdTime = models.DateTimeField('创建时间', db_column='created_time')
    # blank=True -- 是针对表单的，如果 blank=True，表示你的表单填写该字段的时候可以不填
    # null=True -- null 是针对数据库而言，如果 null=True, 表示数据库的该字段可以为空ss
    updatedTime = models.DateTimeField('更新时间', db_column='updated_time', null=True, blank=True)

    # 后台admin中显示，在一对多选择的时候会显示名称，否则显示ArticleCategory object
    def __str__(self):
        return self.categoryName

    class Meta:
        # 指定表名
        db_table = 'article_category'
        '''
            models.Model类的内部类Meta，有两个特殊的选项：verbose_name和verbose_name_plural。
            顾名思义，verbose_name为model提供了一个更容易让人阅读的名称，而verbose_name_plural则是这个名称的复数形式
        '''
        verbose_name = '文章类型'
        verbose_name_plural = '文章类型'


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
    # id = models.IntegerField('主键', primary_key=True, db_column='id')
    id = models.AutoField(primary_key=True)
    articleTitle = models.CharField('主题', max_length=30, db_column='article_title')
    articleContent = models.TextField('内容', max_length=1000, db_column='article_content')
    # 一对多(一个Article对应多个ArticleCategory) on_delete=models.CASCADE 级联删除，也就是当删除主表的数据时候从表中的数据也随着一起删除
    articleCategory = models.ForeignKey('ArticleCategory', db_column='article_category_id', on_delete=models.CASCADE,null=True)
    # 设定值让status进行选择，默认为default=1 表示有效(类似于select功能)
    status_val = (('1', u'有效'), ('0', u'无效'))
    status = models.CharField('状态', choices=status_val, max_length=1, db_column='status', default=1)
    createdTime = models.DateTimeField('创建时间', db_column='created_time')
    # blank=True -- 是针对表单的，如果 blank=True，表示你的表单填写该字段的时候可以不填
    # null=True -- null 是针对数据库而言，如果 null=True, 表示数据库的该字段可以为空
    updatedTime = models.DateTimeField('更新时间', db_column='updated_time', null=True, blank=True)

    class Meta:
        # 指定表名
        db_table = 'article'
        verbose_name = '文章'
        verbose_name_plural = '文章'


class ArticleEncoder(json.JSONDecoder):
    def deault(self, field):
        if isinstance(field, datetime):
            return field.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(field, date):
            return field.strftime('%Y-%m-%d')
        return json.JSONDecoder.default(self, field)
