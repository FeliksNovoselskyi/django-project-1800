from django.shortcuts import render


# Create your views here.
def render_index(request):

    name = "arseniy"

    list_products = ["banana", "persimmon", "kiwi"]

    return render(
        request=request,
        template_name="blog_app/index.html",
        # несколько значений

        # контекст шаблона
        # значения

        # context -
        # контекст в формате словаря
        context={
            "name": name,
            "list_products": list_products
        }
    )

