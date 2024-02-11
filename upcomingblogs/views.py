from rest_framework import generics, permissions
from .models import UpcomingBlog
from .serializers import UpcomingBlogSerializer
from pp5_api.permissions import IsOwnerOrReadOnly


class UpcomingBlogList(generics.ListCreateAPIView):
    """
    API endpoint that allows creation and listing of upcoming blogs.
    """
    serializer_class = UpcomingBlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Retrieve all upcoming blogs.
        """
        return UpcomingBlog.objects.all()

    def perform_create(self, serializer):
        """
        Create a new upcoming blog instance.
        """
        serializer.save(owner=self.request.user)


class UpcomingBlogDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows retrieving, updating, and
    deleting a specific upcoming blog.
    """
    serializer_class = UpcomingBlogSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        """
        Retrieve all upcoming blogs.
        """
        return UpcomingBlog.objects.all()
