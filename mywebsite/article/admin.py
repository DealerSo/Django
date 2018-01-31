from django.contrib import admin
from article.models import *


# Register your models here.

class ArticleCategroyAdmin(admin.ModelAdmin):
    # list_display 必须是一个tuple(元组)
    list_display = ('categoryCode', 'categoryName', 'createdTime', 'updatedTime')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('articleTitle', 'articleContent', 'articleCategory', 'createdTime', 'updatedTime')


admin.site.register(ArticleCategory, ArticleCategroyAdmin)
admin.site.register(Article, ArticleAdmin)
