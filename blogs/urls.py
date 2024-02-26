# urls.py

from django.urls import path
from blogs.views import BlogList, BlogDetail, BlogCategoryList

urlpatterns = [
    path("blogs/", BlogCategoryList.as_view(), name="blog-categories"),
    path("blogs/<str:category>/", BlogList.as_view(), name="blog-list"),
    path(
        "blogs/<str:category>/<int:pk>/",
        BlogDetail.as_view(),
        name="blog-detail",
    ),  # URL pattern for a specific blog detail
]
