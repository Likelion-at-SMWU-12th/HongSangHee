from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Post(models.Model):
    title = models.CharField('제목',max_length=100)
    image = models.ImageField('이미지', null=True, blank=True)
    content = models.TextField('내용')
    created_at = models.DateTimeField('작성일',auto_now_add=True)
    updated_at = models.DateTimeField('최종 수정일',null=True, blank=True, auto_now_add=True)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE,verbose_name='작가', null=True, blank=True)
    view_count = models.IntegerField('조회수', default = 0)

    def __str__(self):
        return f'{self.pk}. {self.title}'
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    writer=models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='작성자', null = True)
    content = models.TextField('내용')
    created_at = models.DateTimeField('작성일',auto_now_add=True)
