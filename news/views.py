from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView



# Create your views here.
def news(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news.html', {'news': news})


class ArticleDetailView(DetailView):
    model = Articles
    template_name = 'news/detail-view.html'
    context_object_name = 'article'


class ArticleEditView(UpdateView):
    model = Articles
    template_name = 'news/edit-article.html'

    form_class = ArticlesForm

class ArticleDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/article-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = 'Form error'    

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)