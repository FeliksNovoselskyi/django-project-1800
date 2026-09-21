from django.shortcuts import render

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