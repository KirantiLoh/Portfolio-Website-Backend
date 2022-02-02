from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.timezone import now

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField('image')
    desc = models.TextField()
    url = models.URLField()
    link_frontend = models.URLField(null=True, blank=True)
    link_backend = models.URLField(null=True, blank=True)
    date_created = models.DateTimeField(default=now)
    show_project = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['-date_created']