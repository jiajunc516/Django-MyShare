from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

class Image(models.Model):

    user = models.ForeignKey(
        to = User,
        on_delete = models.CASCADE,
        related_name = "images_creater"
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField()
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True, db_index=True)
    image = models.ImageField(upload_to="images/%Y/%m/%d/")

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
    # "key: app_name in urls.py, value: url name in urls.py"
        return reverse("image_app:image_detail", args={self.id, self.slug})
