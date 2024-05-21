from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Post (models.Model):

    image = models.ImageField(verbose_name='이미지', null=True, blank=True)
    contentn = models.TextField('내용')
    created_at = models.DateTimeField('작성일', auto_now_add=True)
    view_count = models.IntegerField('조회수', default = 0)
    writer=models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='작성자', null=True, blank=True)

class Student(models.Model):
    name = models.CharField(max_length=100)
    studentNumber = models.IntegerField('학번',default = 24)
    contentn = models.TextField('자기소개')
    image = models.ImageField(verbose_name='이미지')
    created_at = models.DateTimeField('작성일')
    
    def __str__(self):
        return f'{self.pk}. {self.name}'
    
class Comment(models.Model):
    content=models.TextField(verbose_name='내용')
    created_at=models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    post=models.ForeignKey(to='Post', on_delete=models.CASCADE, verbose_name='게시글')
    writer=models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='작성자', null = True)


