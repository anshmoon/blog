from django.contrib import admin
from .models import Post , ContactForm
# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'title', 'desc']


@admin.register(ContactForm)
class ContactFormModelAdmin(admin.ModelAdmin):
 list_display = ['name', 'message']