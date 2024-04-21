from django.shortcuts import render
# from django.http import HttpResponse
from news.models import Articles

# Create your views here.

def index(request):
    data = {
       'title': 'Main page!',
       'news': Articles.objects.order_by('-date')[:9]
    }
    return render(request, 'main/index.html', data)


def search_articles(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        articles = Articles.objects.filter(title__contains=searched)
        return render(request, 'main/search-articles.html', {'searched':searched, 'articles':articles})
    else:
        return render(request, 'main/search-articles.html', {})


def about(request):
    return render(request, 'main/about.html')