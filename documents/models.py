from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_type = models.CharField(max_length=10)
    
    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        # Delete the file from storage
        self.file.delete()
        super().delete(*args, **kwargs)