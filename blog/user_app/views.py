from django.shortcuts import render
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


# Саша
# Собрать функцию отображения к шаблону author_view.html
def render_author_view(request, pk):
    author = Author.objects.get(pk = pk)
    return render(
        request=request,
        template_name="user_app/author_view.html",
        context = {
            "author": author,
        }
    )