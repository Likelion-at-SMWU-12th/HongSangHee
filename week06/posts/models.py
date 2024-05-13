from django.db import models

# Create your models here.

class Post (models.Model):

    image = models.ImageField(verbose_name='이미지')
    contentn = models.TextField('내용')
    created_at = models.DateTimeField('작성일')
    view_count = models.IntegerField('조회수', default = 0)

class Student(models.Model):
    name = models.CharField(max_length=100)
    studentNumber = models.IntegerField('학번',default = 24)
    contentn = models.TextField('자기소개')
    image = models.ImageField(verbose_name='이미지')
    created_at = models.DateTimeField('작성일')
    
    def __str__(self):
        return f'{self.pk}. {self.name}'


