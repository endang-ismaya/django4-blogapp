from django.contrib import admin
from .models import Post, Tag, Comment, Profile


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "image",
        "view_count",
        "slug",
        "last_updated",
        "is_featured",
    )
    search_fields = ("title",)
    search_help_text = "Write in your query and hit enter!"
    fields = (
        "title",
        "author",
        "content",
        "image",
        "tags",
        "view_count",
        "is_featured",
    )


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "profile_image",
        "slug",
        "bio",
    )
    fields = ("user", "profile_image", "bio")


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Profile, ProfileAdmin)
