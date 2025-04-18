from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class JobPost(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')
    posted_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title