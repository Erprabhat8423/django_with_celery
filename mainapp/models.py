from django.db import models

# Create your models here.
class SpActivityLogs(models.Model):
    package_name = models.CharField(max_length=100, blank=True, null=True)
    app_name = models.CharField(max_length=100, blank=True, null=True)
    developer = models.CharField(max_length=100, blank=True, null=True)
    Price = models.FloatField(max_length=100, blank=True, null=True)
    Rating = models.FloatField(max_length=10, blank=True, null=True)
    description = models.TextField( blank=True, null=True)
    icon_url = models.URLField(blank=True, null=True)
    cover_image = models.CharField(max_length=500,blank=True, null=True)
   
