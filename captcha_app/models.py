from django.db import models
from django.contrib.auth.models import User
import secrets

class APIKey(models.Model):
    """
    Model to store the API keys associated with users.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return f"{self.user.username} - {self.key}"

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_key():
        return secrets.token_urlsafe(32)


class Captcha(models.Model):
    """
    Model to store CAPTCHA text, image, and associated data.
    """
    captcha_id = models.CharField(max_length=16, unique=True)
    text = models.CharField(max_length=6)
    image = models.TextField()  # Base64-encoded image string
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return f"CAPTCHA {self.captcha_id}"

