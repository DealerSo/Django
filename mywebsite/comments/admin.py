from django.contrib import admin
from comments.models import *


# Register your models here.

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    # 后端显示字段
    list_display = ('name', 'email', 'phone', 'sex', 'title', 'content', 'status', 'createdTime', 'updatedTime')

    '''
        取消后台这些功能，这些方法都是在ModelAdmin类中
    '''
    def has_add_permission(self, request):
        """ 取消后台添加附件功能 """
        return False

    def has_delete_permission(self, request, obj=None):
        """ 取消后台删除附件功能 """
        return False

    def save_model(self, request, obj, form, change):
        """ 取消后台编辑附件功能 """
        return False