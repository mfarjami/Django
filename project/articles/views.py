from django.shortcuts import render
from .models import *
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

@login_required(login_url="/account/login")
def create_article(request):
    return render(request, 'articles/create_article.html')
    