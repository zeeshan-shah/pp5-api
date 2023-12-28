from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Blog
from .serializers import BlogSerializer
from pp5_api.permissions import IsOwnerOrReadOnly

class BlogList(APIView):
    serializer_class = BlogSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(
            blogs, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class BlogDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BlogSerializer

    def get_object(self, pk):
        try:
            blog = Blog.objects.get(pk=pk)
            self.check_object_permissions(self.request, blog)
            return blog
        except Blog.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        blog = self.get_object(pk)
        serializer = BlogSerializer(
            blog, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        blog = self.get_object(pk)
        serializer = BlogSerializer(
            blog, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        blog = self.get_object(pk)
        blog.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )