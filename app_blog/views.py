from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Post, Comment
from .forms import CommentForm, SubscribeForm

# Create your views here.
def post_page(request, slug):

    try:
        post = Post.objects.get(slug=slug)
        tags = post.tags.all()
        form = CommentForm()
        comments = Comment.objects.filter(post=post, parent=None)

        if request.POST:
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                parent_obj = None
                parent_id = request.POST.get("parent", -1)
                if parent_id != -1:
                    # save reply
                    parent_obj = Comment.objects.get(pk=parent_id)

                    if parent_obj:
                        comment_reply = comment_form.save(commit=False)
                        comment_reply.parent = parent_obj
                        comment_reply.post = post
                        comment_reply.save()

                        return HttpResponseRedirect(
                            reverse("app_blog:post_page", kwargs={"slug": slug})
                        )
                else:
                    comment = comment_form.save(
                        commit=False
                    )  # not saving to db, get the instance of comment
                    comment.post = post
                    comment.save()

                return HttpResponseRedirect(
                    reverse("app_blog:post_page", kwargs={"slug": slug})
                )

        else:
            # increment view_count
            post.view_count = post.view_count + 1
            # save to db
            post.save()

        # return finally
        ctx = {"post": post, "tags": tags, "form": form, "comments": comments}
        return render(request, "app_blog/post.html", ctx)
    except:
        return HttpResponse(f"Post '{slug}' not found")


def index(request):
    # posts = Post.objects.all()
    top_posts = Post.objects.all().order_by("-view_count")[:3]
    recent_posts = Post.objects.all().order_by("-last_updated")[:3]
    featured_posts = Post.objects.filter(is_featured=True)
    featured_post = None
    subscribe_form = SubscribeForm()
    subscribe_successful = None

    if featured_posts:
        featured_post = featured_posts[0]

    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            subscribe_successful = "Subscribed Successfully"
            subscribe_form = SubscribeForm()

    ctx = {
        "top_posts": top_posts,
        "recent_posts": recent_posts,
        "subscribe_form": subscribe_form,
        "subscribe_successful": subscribe_successful,
        "featured_post": featured_post,
    }
    return render(request=request, template_name="app_blog/index.html", context=ctx)


def tag_page(request, slug):
    ctx = {}
    return render(request, "app_blog/tag.html", ctx)
