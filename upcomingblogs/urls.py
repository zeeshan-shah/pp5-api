from django.urls import path
from .views import UpcomingBlogList, UpcomingBlogDetail

urlpatterns = [
    path(
        "upcoming-blogs/",
        UpcomingBlogList.as_view(),
        name="upcoming-blog-list",
    ),
    path(
        "upcoming-blogs/<int:pk>/",
        UpcomingBlogDetail.as_view(),
        name="upcoming-blog-detail",
    ),
]
