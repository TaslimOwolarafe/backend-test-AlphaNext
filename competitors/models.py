from django.db import models

class Competitor(models.Model):
    business_name = models.CharField(max_length=255)
    business_type = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    website_traffic = models.JSONField()
    top_performing_pages = models.JSONField()

    def __str__(self):
        return self.business_name
