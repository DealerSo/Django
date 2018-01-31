# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

'''
    文章app的模块有如下几个：
    (1) 文章分类 ：Java ，Python 等
    (2) 文章 
'''

'''
    (1)文章分类表：article_category包含如下字段
        (A) id 主键
        (B) category_code 分类code
        (C) category_name 分类名称
        (D) status 状态 (1：表示有效,0表示无效)
        (E) created_time 创建时间
        (F) updated_time 更新时间
    (2)文章表：article包含如下字段
        (A) id 主键
        (B) article_title 文章主题
        (C) article_category_id 文章分类(外键)
        (D) article_content 文章内容
        (E) status 状态 (1：表示有效,0表示无效)
        (F) created_time 创建时间
        (G) updated_time 更新时间
'''


class ArticleCategory(models.Model):
    id = models.IntegerField('主键', primary_key=True, db_column='id')
    categoryCode = models.CharField('分类编码', max_length=20, db_column='category_code')
    categoryName = models.CharField('分类名称', max_length=30, db_column='category_name')
    status = models.CharField('状态', max_length=1, db_column='status')
    createdTime = models.DateTimeField('创建时间', db_column='created_time')
    updatedTime = models.DateTimeField('更新时间', db_column='updated_time', null=True, blank=True)

    def __str__(self):
        return self.categoryName

    class Meta:
        # 指定表名
        db_table = 'article_category'


class Article(models.Model):
    id = models.IntegerField('主键', primary_key=True, db_column='id')
    articleTitle = models.CharField('主题', max_length=30, db_column='article_title')
    articleContent = models.CharField('内容', max_length=500, db_column='article_content')
    # 一对多(一个Article对应多个ArticleCategory) on_delete=models.CASCADE 级联删除，也就是当删除主表的数据时候从表中的数据也随着一起删除
    articleCategory = models.ForeignKey('ArticleCategory', db_column='article_category_id', on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField('状态', max_length=1, db_column='status')
    createdTime = models.DateTimeField('创建时间', db_column='created_time')
    updatedTime = models.DateTimeField('更新时间', db_column='updated_time', null=True, blank=True)

    class Meta:
        # 指定表名
        db_table = 'article'
