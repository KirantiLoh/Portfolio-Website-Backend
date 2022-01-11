from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = CloudinaryField('image')
    content = models.TextField(max_length=5000)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        ordering = ['-date_created']