from rest_framework.serializers import ModelSerializer
from .models import Post, Comment

class PostModelSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostListSerializer(PostModelSerializer):
    pass

class PostListSerializer(PostModelSerializer):
    class Meta(PostModelSerializer.Meta):
        fields = ['id', 'writer', 'contentn', 'created_at', 'view_count']
        depth = 1
    #PostModelSerializer는 post 모델을 사용하고 있으므로 그 field는 post 모델에 정의된 field 이름과 일치해야함

class PostCreateSerializer(PostModelSerializer):
    class Meta(PostModelSerializer.Meta):
        fields = ['image', 'content']

class PostRetrieveSerializer(PostModelSerializer):
    class Meta(PostModelSerializer.Meta):
        depth = 1

class CommentListModelSerializer(ModelSerializer):
    class Meta: 
        model = Comment
        fields = '__all__'