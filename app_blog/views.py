from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

# Create your views here.
def post_page(request, slug):

    try:
        post = Post.objects.get(slug=slug)
        ctx = {"post": post}
        return render(request, "app_blog/post.html", ctx)
    except:
        return HttpResponse(f"Post '{slug}' not found")


def index(request):
    posts = Post.objects.all()
    ctx = {"posts": posts}
    return render(request=request, template_name="app_blog/index.html", context=ctx)
