from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from articles.forms import ArticleForm 

# Create your views here.

def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ArticleForm(request.POST)
            if form.is_valid():
                article = form.save(commit=False)
                article.user = request.user  # 오타 수정
                article.save()
                return redirect('articles:index')
        else:
            article_form = ArticleForm()
        context = {
            'article_form': article_form
        }
        return render(request, 'articles/forms.html', context)
    else:
        return redirect('accounts:login')

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else:
        # GET : Form을 제공
        article_form = ArticleForm(instance=article)
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/forms.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)
