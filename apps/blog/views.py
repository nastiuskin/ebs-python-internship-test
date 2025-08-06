from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, ListCreateAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from apps.blog.models import Blog, Category, Comment
from apps.blog.serializers import BlogSerializer, CategorySerializer, CommentSerializer
from apps.common.permissions import ReadOnly
from rest_framework import mixins

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BlogListView(ListCreateAPIView):
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Blog.objects.all()


class BlogItemView(RetrieveAPIView):
    serializer_class = BlogSerializer
    permission_classes = (AllowAny,)
    queryset = Blog.objects.all()


class BlogCommentView(CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (AllowAny,)
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        blog_id = self.kwargs['pk']
        serializer.save(blog_id=blog_id)


