from django.contrib import admin
from .models import Image

# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "user", "created")
    list_filter = ("user", "created")
    search_fields = ("title", "description")
    ordering = ("user", "created")