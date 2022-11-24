from django.shortcuts import render
from .models import Post

# Create your views here.
def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    ctx = {"post": post}
    return render(request, "app_blog/post.html", ctx)
