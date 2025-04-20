from django.urls import path
from .views import (
    CompanyListCreateAPIView,
    CompanyRetrieveUpdateAPIView,
    CompanyDeleteAPIView,
    JobPostListCreateAPIView,
    JobPostRetrieveAPIView,
    JobPostDeleteAPIView
)

urlpatterns = [
    # Company endpoints
    path('companies/', CompanyListCreateAPIView.as_view(), name='company-list-create'),
    path('companies/<int:pk>/', CompanyRetrieveUpdateAPIView.as_view(), name='company-detail'),
    path('companies/update/<int:pk>/', CompanyRetrieveUpdateAPIView.as_view(), name='company_update_view'),
    path('companies/delete/<int:pk>/', CompanyDeleteAPIView.as_view(), name='company_delete_view'),
    
    # JobPost endpoints
    path('jobs/', JobPostListCreateAPIView.as_view(), name='job-list-create'),
    path('jobs/<int:pk>/', JobPostRetrieveAPIView.as_view(), name='job-detail'),
    path('jobs/update/<int:pk>/', JobPostRetrieveAPIView.as_view(), name='jobpost_update_view'),
    path('jobs/delete/<int:pk>/', JobPostDeleteAPIView.as_view(), name='jobpost_delete_view'),
]
