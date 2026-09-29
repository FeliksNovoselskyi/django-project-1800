from django.shortcuts import render

from .models import User


# Create your views here.
def render_auth(request):

    # Получить все записи модели User
    users = User.objects.all()

    return render(
        request=request,
        template_name="user_app/auth.html",
        context={"users": users}
    )

def render_reg(request):
    return render(
        request=request,
        template_name="user_app/reg.html"
    )
