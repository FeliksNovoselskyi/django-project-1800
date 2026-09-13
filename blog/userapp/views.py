from django.shortcuts import render
# Create your views here.
def render_reg(request):

    return render(request, 'userapp/reg.html')
