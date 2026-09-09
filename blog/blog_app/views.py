from django.shortcuts import render

# Create your views here.
def render_index(request):
    
    return render(
        request=request,
        template_name="blog_app/index.html"
    )
    


# функция отображения, принимает в себя обязательный аргумент request
# render() принимает в себя request
