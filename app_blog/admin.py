from django.contrib import admin
from .models import Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "image", "view_count", "slug", "last_updated")
    search_fields = ("title",)
    search_help_text = "Write in your query and hit enter!"
    fields = ("title", "content", "image", "tags", "view_count")


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
