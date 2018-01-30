from django.db import models

# Create your models here.

'''
    这里需要注意一下几点
    (1) model的类名必须和数据库中的表名对相应
    (2) model必须继承Model
'''


# class Student(models.Model):
#     id = models.IntegerField()
#     age = models.IntegerField()
#     name = models.CharField(max_length=50)
#
#     # 将对象以str的方式显示出来
#     def __str__(self):
#         return self.name

