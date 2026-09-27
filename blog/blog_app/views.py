from django.shortcuts import render
from blog_app.models import Post

# Create your views here.
def render_index(request):
    # получает все записи из таблицы
    posts_list = Post.objects.all()

    return render(
        request=request,
        template_name="blog_app/index.html",
        context={
            "posts_list": posts_list
        }
    )

