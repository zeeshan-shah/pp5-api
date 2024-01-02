from django.urls import path
from blogs import views

urlpatterns = [
    path('blogs/', views.BlogList.as_view()),
    path('blogs/<int:pk>/', views.BlogDetail.as_view()),
]