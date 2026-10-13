from blog_app.models import Post
from django.shortcuts import render


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
