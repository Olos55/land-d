from django.db import models
from django.contrib.auth.models import User

class Land(models.Model):
    title_deed_number = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title_deed_number

class Dispute(models.Model):
    land = models.ForeignKey(Land, on_delete=models.CASCADE)
    claimant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='claimant')
    respondent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='respondent')
    description = models.TextField()
    status = models.CharField(max_length=50, choices=[('open', 'Open'), ('closed', 'Closed')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.claimant} vs {self.respondent} - {self.status}"


# Create your models here.
