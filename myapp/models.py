
from django.db import models
from djongo import models as djongo_models
from django.contrib.auth.models import AbstractUser
import pymongo


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, null=True, blank=True)

class UserActivity(djongo_models.Model):
    user_id = djongo_models.IntegerField()
    action = djongo_models.CharField(max_length=255)
    timestamp = djongo_models.DateTimeField()
    location = models.JSONField(null=True, blank=True)  # Geo-location field
    
    class Meta:
        indexes = [
            # Create a text index for the action field
            djongo_models.Index(fields=['action'], name='action_text_index'),
        ]