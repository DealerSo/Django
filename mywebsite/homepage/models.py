from django.db import models

# Create your models here.

'''
    这里需要注意一下几点
    (1) model的类名必须和数据库中的表名对相应
    (2) model必须继承Model
'''


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    age = models.IntegerField()
    name = models.CharField(max_length=50)
    createdTime = models.DateTimeField()

    # 将对象以str的方式显示出来
    def __str__(self):
        return self.name

    # 必须要加，指定数据库表的名字，否则查询的时候会将app的名字加上去作为表名
    # 如:homepage_student作为表名
    class Meta:
        db_table = 'student'
