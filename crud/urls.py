from django.urls import path
from .views import (
    CompanyListCreateAPIView,
    CompanyRetrieveUpdateAPIView,
    JobPostListCreateAPIView,
    JobPostRetrieveAPIView
)

urlpatterns = [
    # Company endpoints
    path('companies/', CompanyListCreateAPIView.as_view(), name='company-list-create'),
    path('companies/<int:pk>/', CompanyRetrieveUpdateAPIView.as_view(), name='company-detail'),

    # JobPost endpoints
    path('jobs/', JobPostListCreateAPIView.as_view(), name='job-list-create'),
    path('jobs/<int:pk>/', JobPostRetrieveAPIView.as_view(), name='job-detail'),
]
