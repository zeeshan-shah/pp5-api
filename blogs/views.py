from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from pp5_api.permissions import IsOwnerOrReadOnly
from .models import Blog
from .serializers import BlogSerializer


class BlogList(generics.ListCreateAPIView):
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Blog.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Blog.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')