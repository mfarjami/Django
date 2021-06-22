from django.shortcuts import redirect, render
from .models import *
from .forms import CreateArticle
from django.contrib.auth.decorators import login_required
# Create your views here.
def articles_list(request):
    context = {
        "articles" : Article.objects.all().order_by('-date')
    }
    return render(request, 'articles/articleslist.html', context)

def article_detail(request, slug):
    context = {
        "article" : Article.objects.get(slug=slug)
    }
    return render(request, 'articles/articledetail.html', context)

@login_required(login_url="/accounts/login")
def create_article(request):
    if request.method == 'POST':
        form = CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            return redirect('articles:list')
    else:
        form = CreateArticle()

    return render(request, 'articles/create_article.html', {'form':form})
    