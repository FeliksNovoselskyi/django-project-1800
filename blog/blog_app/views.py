from blog_app.models import Post
from django.shortcuts import render


# Create your views here.
def render_index(request):

    posts_list = Post.objects.all()

    return render(
        request=request,
        template_name="blog_app/index.html",
        context={
            "posts_list": posts_list
        }
    )


# Миша Панков: создать функцию отображения для шаблона post_view.html
def render_post(request, pk):
    
    print(pk)
    
    # Получить по pk запись поста (Post)
    post = Post.objects.get(pk=pk)
    
    # Передать полученный пост на шаблон
    return render(request=request,template_name="blog_app/post_view.html", context= {"post": post})
