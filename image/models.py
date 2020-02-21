from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from taggit.managers import TaggableManager

class Image(models.Model):

    user = models.ForeignKey(
        to = User,
        on_delete = models.CASCADE,
        related_name = "images_creater"
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField(null=True, blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    image = models.ImageField(upload_to="images/%Y/%m/%d/")

    user_like = models.ManyToManyField(
        to=User,
        related_name="images_liked",
        blank=True
    )
    tags = TaggableManager()

    class Meta:
        ordering = ("-created", )

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
    # "key: app_name in urls.py, value: url name in urls.py"
        return reverse("image_app:image_detail", args=[self.id, self.slug])

class Comment(models.Model):
    
    user = models.ForeignKey(
        to = User,
        on_delete = models.CASCADE,
        related_name = "comment_creater"
    )
    image = models.ForeignKey(
        to = Image,
        on_delete = models.CASCADE,
        related_name = "comment"
    )
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ("-created", )
    
    def __str__(self):
        return "{} makes a comment on {}".format(self.user.username, self.image)