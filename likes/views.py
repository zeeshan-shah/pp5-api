from rest_framework import generics, permissions
from pp5_api.permissions import IsOwnerOrReadOnly
from likes.models import Like
from likes.serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer

    def get_queryset(self):
        return Like.objects.filter(blog_id=self.kwargs.get('blog_pk'))

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer

    def get_queryset(self):
        return Like.objects.filter(blog_id=self.kwargs.get('blog_pk'))
