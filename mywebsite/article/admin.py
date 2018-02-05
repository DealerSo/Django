from django.contrib import admin
from article.models import *


# Register your models here.

# @admin.register(ArticleCategory) 注册这个app,等价于 admin.site.register(ArticleCategory, ArticleCategroyAdmin)
@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    # list_display 必须是一个tuple(元组)
    list_display = ('categoryCode', 'categoryName', 'createdTime', 'updatedTime')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 显示的字段是一个元组
    list_display = ('articleTitle', 'articleContent', 'articleCategory', 'createdTime', 'updatedTime')
    # 查询的字段是是一个列表
    search_fields = ['articleTitle']

#admin.site.register(ArticleCategory, ArticleCategroyAdmin)
#admin.site.register(Article, ArticleAdmin)
