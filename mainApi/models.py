
from django.db import models

class ContactForm(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    consultation_type = models.CharField(max_length=255, choices=[
        ('video', 'video'),
        ('call', 'call'),
    ])
    service_intrest = models.CharField(max_length=255, choices=[
        ('strength', 'strength'),
        ('weight_loss', 'weight_loss'),
        ('custom diet', 'custom diet'),
        ('online coaching', 'online coaching'),
        ('not sure', 'not sure'),
    ])
    pacakage_intrest = models.CharField(max_length=255, choices=[
        ('basic', 'basic'),
        ('premium', 'premium'),
        ('vip', 'vip'),
        ('not sure', 'not sure'),
    ])
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
