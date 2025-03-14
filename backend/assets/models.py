from django.db import models
from django.conf import settings

class Asset(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assets')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='assets/')
    created_at = models.DateTimeField(auto_now_add=True)

class Purchase(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='purchases')
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='purchases')
    progress = models.IntegerField(default=0)  # e.g., percent progress (0-100)
    created_at = models.DateTimeField(auto_now_add=True)
