from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('creator', 'Creator'),
        ('customer', 'Customer'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

class Asset(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assets')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='assets/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Purchase(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='purchases')
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    purchase_date = models.DateTimeField(auto_now_add=True)
    progress = models.IntegerField(default=0)  # Percentage progress updated by creator
    status = models.CharField(max_length=20, default='pending')
    request_start_date = models.DateField(null=True, blank=True)
    request_end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Purchase {self.id} by {self.customer.username}"

class ChatMessage(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message by {self.sender.username} at {self.timestamp}"
