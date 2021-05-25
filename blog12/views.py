
from django.shortcuts import render
from blog12.models import *
# Create your views here.
def home(request):
    data = Article.objects.all()
    context = {'data': data}
    return render(request, 'blog.html', context)