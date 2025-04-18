from rest_framework import serializers
from .models import Company, JobPost

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class JobPostSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    company_id = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(), source='company', write_only=True)

    class Meta:
        model = JobPost
        fields = ['id', 'title', 'description', 'location', 'salary', 'posted_date', 'company', 'company_id']
