from blog_app.models import Post
from django import forms
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from .forms import PostForm


# Create your views here.
def render_index(request):

    posts_list = Post.objects.all()

    print(posts_list)

    return render(
        request=request,
        template_name="blog_app/index.html",
        context={
            "posts_list": posts_list
        }
    )

# Арсений
# собрать функцию отображения для страницы конкретного поста
def render_post(request, pk):

    post = Post.objects.get(pk=pk)

    # post_view.html
    return render(
        request=request,
        template_name="blog_app/post_view.html",
        context={
            "post": post
        }
    )

def render_form(request):
    form = PostForm()
    
    return render(
        request=request,
        template_name="blog_app/form.html",
        context={
            "form": form
        }
    )


@require_POST
def handle_form(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    # Миша Морозов.
    # Получить значения полей is_publish, author_id
    is_publish = request.POST.get("is_publish")
    author_id = request.POST.get("author_id")

    if is_publish == 'on':
        is_publish = True

    if not title and not content:
        return JsonResponse(
            data={"error": "Title and content cannot be empty."},
            status=400
        )

    post =Post.objects.create(
        title=title,
        content=content,
        is_publish=is_publish,
        author_id=author_id
    )

    return redirect(to="main_page")
