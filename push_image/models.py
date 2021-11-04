from django.contrib.postgres.fields.jsonb import JSONField
from django.db import models

# Create your models here.
from django.db import models


class ArticleTag(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, )
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE, )

    created_at = models.DateTimeField(auto_now_add=True, )

    class Meta:
        db_table = 'articles_tags'


class Article(models.Model):
    name = models.CharField(max_length=100)
    tags = models.ManyToManyField('Tag', through='ArticleTag')

    class Meta:
        db_table = 'articles'


class Tag(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    data = JSONField(null=True)
    class Meta:
        db_table = 'tags'


class tags_view(models.Model):
    #branchid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tags_view'

class Student(models.Model):
    student_name = models.CharField(max_length=100)

class Teacher(models.Model):
    teacher_name=models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name='teachers')
