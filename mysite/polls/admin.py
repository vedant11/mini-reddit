from django.contrib import admin

# Register your models here.
from .models import Post, Choice


class PostAdmin(admin.ModelAdmin):
    fields = ["pub_date", "post_text", "post_message"]


admin.site.register(Post, PostAdmin)
admin.site.register(Choice)
