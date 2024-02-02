from rest_framework import generics, permissions
from .models import UpcomingBlog
from .serializers import UpcomingBlogSerializer

class UpcomingBlogList(generics.ListCreateAPIView):
    serializer_class = UpcomingBlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return UpcomingBlog.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UpcomingBlogDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UpcomingBlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return UpcomingBlog.objects.all()
