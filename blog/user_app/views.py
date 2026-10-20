from blog_app.models import Post
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from user_app.models import Author


# Create your views here.
def render_auth(request):

    return render(
        request=request,
        template_name="user_app/auth.html"
    )

def render_reg(request):
    return render(
        request=request,
        template_name="user_app/reg.html"
    )

def render_author_view(request, pk):

    # author = Author.objects.get(pk = pk)

    # 404 - not found
    # получить объект или ошибку 404

    # get_object_or_404 - получает объект или возвращает ошибку 404
    author = get_object_or_404(
        Author,
        # может быть несколько полей
        pk = pk,
        name="Feliks"
    )

    print(author) # Author object (1)

    # 1.
    # posts = Post.objects.filter(
    #     author_id = author.pk
    # )

    # 2.
    # Получаем доступ к постам автора
    # blog_app.Post.None - QuerySet
    # QuerySet - набор записей из БД
    posts = author.posts.all()

    # <QuerySet [<Post: Post object (1)>]>

    print(posts)

    return render(
        request=request,
        template_name="user_app/author_view.html",
        context = {
            "author": author,
            # Передать посты на шаблон
            "posts": posts
        }
    )