from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics

class CompanyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
class CompanyRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = 'pk'
    
class CompanyDeleteAPIView(generics.DestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = 'pk'

class JobPostListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = JobPostSerializer

    def get_queryset(self):
        company_id = self.request.query_params.get('company')
        if company_id:
            return JobPost.objects.filter(company_id=company_id)
        return JobPost.objects.all()

class JobPostRetrieveAPIView(generics.RetrieveAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    lookup_field = 'pk'
    
class JobPostDeleteAPIView(generics.DestroyAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    lookup_field = 'pk'   