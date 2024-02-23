from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe
# from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm
# from django.contrib import messages


# Create your views here.

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

@require_safe
def index(request):
    articles = Article.objects.all()
    context = {"articles":articles}
    return render(request, "articles/index.html", context)

def article_new(request):
    return render(request, "articles/new_article.html")

# @login_required
def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})

# @login_required
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_detail.html', {'article': article})


# @login_required
def edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {"article": article}
    return render(request, "articles/edit.html", context)


# @login_required
def update_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm(instance=article)

    return render(request, 'update_article.html', {'form': form, 'article': article})


def delete_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == "POST":
        article.delete()
        return redirect("articles:index")
    context = {"article": article}
    return render(request, "articles/delete.html", context)

