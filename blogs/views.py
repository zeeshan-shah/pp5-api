from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from pp5_api.permissions import IsOwnerOrReadOnly
from .models import Blog
from .serializers import BlogSerializer, BlogCategorySerializer
from django.http import Http404


class BlogCategoryList(generics.ListAPIView):
    """
    API endpoint that returns a list of blog categories.
    """
    serializer_class = BlogCategorySerializer

    def get_queryset(self):
        """
        Get queryset of blog categories.
        """
        return [{'category': choice[0]} for choice in Blog.CATEGORY_CHOICES]


class BlogList(generics.ListCreateAPIView):
    """
    API endpoint that returns a list of blogs or creates a new blog.
    """
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
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

    def get_queryset(self):
        """
        Get queryset of blogs.
        """
        category = self.kwargs.get('category')

        # Check if the category is valid based on the
        # first elements of the tuples in CATEGORY_CHOICES
        if category not in [choice[0] for choice in Blog.CATEGORY_CHOICES]:
            raise Http404("Invalid category")

        queryset = Blog.objects.annotate(
            likes_count=Count('likes', distinct=True),
            comments_count=Count('comment', distinct=True)
        ).order_by('-created_at')

        if category:
            queryset = queryset.filter(category=category)

        return queryset

    def perform_create(self, serializer):
        """
        Perform creation of a new blog.
        """
        category = self.kwargs.get('category')

        # Check if the category is valid based on the
        #  first elements of the tuples in CATEGORY_CHOICES
        if category not in [choice[0] for choice in Blog.CATEGORY_CHOICES]:
            raise Http404("Invalid category")

        serializer.save(owner=self.request.user, category=category)


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that retrieves, updates or deletes a specific blog.
    """
    serializer_class = BlogSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Blog.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
