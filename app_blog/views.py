from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.
def post_page(request, slug):

    try:
        post = Post.objects.get(slug=slug)
        tags = post.tags.all()
        form = CommentForm()
        comments = Comment.objects.filter(post=post)

        if request.POST:
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                comment = comment_form.save(
                    commit=False
                )  # not saving to db, get the instance of comment
                comment.post = post
                comment.save()

        # increment view_count
        post.view_count = post.view_count + 1
        # save to db
        post.save()
        ctx = {"post": post, "tags": tags, "form": form, "comments": comments}
        return render(request, "app_blog/post.html", ctx)
    except:
        return HttpResponse(f"Post '{slug}' not found")


def index(request):
    posts = Post.objects.all()
    ctx = {"posts": posts}
    return render(request=request, template_name="app_blog/index.html", context=ctx)
