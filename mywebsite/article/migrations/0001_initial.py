# Generated by Django 2.0.1 on 2018-02-05 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.IntegerField(db_column='id', primary_key=True, serialize=False, verbose_name='主键')),
                ('articleTitle', models.CharField(db_column='article_title', max_length=30, verbose_name='主题')),
                ('articleContent', models.CharField(db_column='article_content', max_length=500, verbose_name='内容')),
                ('status', models.CharField(db_column='status', max_length=1, verbose_name='状态')),
                ('createdTime', models.DateTimeField(db_column='created_time', verbose_name='创建时间')),
                ('updatedTime', models.DateTimeField(blank=True, db_column='updated_time', null=True, verbose_name='更新时间')),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.IntegerField(db_column='id', primary_key=True, serialize=False, verbose_name='主键')),
                ('categoryCode', models.CharField(db_column='category_code', max_length=20, verbose_name='分类编码')),
                ('categoryName', models.CharField(db_column='category_name', max_length=30, verbose_name='分类名称')),
                ('status', models.CharField(db_column='status', max_length=1, verbose_name='状态')),
                ('createdTime', models.DateTimeField(db_column='created_time', verbose_name='创建时间')),
                ('updatedTime', models.DateTimeField(blank=True, db_column='updated_time', null=True, verbose_name='更新时间')),
            ],
            options={
                'db_table': 'article_category',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='articleCategory',
            field=models.ForeignKey(blank=True, db_column='article_category_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='article.ArticleCategory'),
        ),
    ]
