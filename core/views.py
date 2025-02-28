from django.shortcuts import render
from . import models

def home(request):
    return render(request, 'core/home.html')


def news_list(request):
    news_items = models.News.objects.all()
    for news in news_items:
        news.header = news.get_translated_header()
        news.content = news.get_translated_content()
    return render(request, 'core/news.html', {'news_items': news_items})
