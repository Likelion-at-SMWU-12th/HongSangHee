from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import action
from .models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

from .serializers import PostSerializer, CommentSerializer

# Create your views here.

class PostModelView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentModelView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @action(detail=True, methods=['POST'])
    def create_comment(self, request, pk):
        #post_id를 통해 해당 post 객체 받아오기
        post = get_object_or_404(Post, pk = pk)
        #CommentSerializer 객체를 생성
        serializer = self.get_serializer(data=request.data)
        #유효성 검사
        serializer.is_valid(raise_exception=True)
        #댓글을 post 객체와 연결시켜서 저장하기
        serializer.save(post=post)
        #댓글 data를 반환하도록 따로 설정함
        return Response(serializer.data, status=status.HTTP_201_CREATED)