from django.contrib import admin
from .models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("user_from", "user_to", "created")
    list_filter = ("user_from", "user_to", "created")
    search_fields = ("user_from", "user_to")
    ordering = ("user_from", "user_to", "created")