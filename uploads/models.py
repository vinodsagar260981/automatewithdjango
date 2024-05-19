from django.db import models

# Create your models here.
class Upload(models.Model):
    file = models.FileField(upload_to='uploads/', blank=True)
    model_name = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.model_name