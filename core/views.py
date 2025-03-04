from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from . import models

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def news_home(request):
    """Fetch the latest, trending, and all news for display."""
    top_news = models.News.objects.exclude(unique_id="").order_by('-created_at').first()  # Most recent news
    latest_news = models.News.objects.exclude(unique_id="").order_by('-created_at')[1:7]  # Latest 6 news excluding top
    trending_news = models.News.objects.exclude(unique_id="").order_by('-created_at')[:5]  # Top 5 trending news

    context = {
        'top_news': top_news,
        'latest_news': latest_news,
        'trending_news': trending_news
    }
    return render(request, 'core/news.html', context)

def news_detail(request, unique_id):
    """Fetch a specific news article by unique_id."""
    news = get_object_or_404(models.News, unique_id=unique_id)
    return render(request, 'core/news_detail.html', {'news': news})

def contact(request):
    return render(request, 'core/contact.html')
