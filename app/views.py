from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from app.models import Article

def home(request):
    obj = Article.objects.all()[:3]
    context = {
        'title': 'Simple blog',
        'articles': obj,
    }
    return render(request, 'blog/home.html', context)

def index(request):
    obj = Article.objects.all()
    paginator = Paginator(obj, 2)
    page_number = request.GET.get('page')
    context = {
        'page_obj': paginator.get_page(page_number),
        'page_number': page_number,
    }
    return render(request, 'blog/index.html', context)

def article(request, id):
    obj = Article.objects.get(id=id)
    context = {
        'article': obj,
    }
    return render(request, 'blog/article.html', context)
