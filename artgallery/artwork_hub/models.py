from django.db import models
from taggit.managers import TaggableManager
from django.conf import settings
from datetime import datetime    

# Create your models here.

class Artwork(models.Model):
    name = models.CharField(max_length=256) 
    description = models.TextField()
    species_img = models.ImageField(upload_to = 'artwork/')
    tags = TaggableManager()

    created_at = models.DateTimeField(blank=True, default=datetime.now)
    updated_at = models.DateTimeField(blank=True, default=datetime.now)
    
    class Meta:
        verbose_name = "Art work"
        verbose_name_plural = "Art work"


from django.core.validators import MinLengthValidator
class Pic(models.Model) :
    title = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    text = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Picture
    picture = models.BinaryField(null=True, blank=True, editable=True)
    content_type = models.CharField(max_length=256, null=True, blank=True, 
            help_text='The MIMEType of the file')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        return self.title
