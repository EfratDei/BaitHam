from django.shortcuts import render
from .models import articles
from .filters import articleFilter


def all_articles(request):
    article = articles.objects.all()
    myfilter = articleFilter(request.GET, queryset=article)
    article = myfilter.qs
    context = {'article': article, 'myfilter': myfilter}
    return render(request, 'Article/articles.html', context)