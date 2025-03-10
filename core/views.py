
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from . import models  
from datetime import datetime
from django.utils.translation import get_language


def home(request):
    return render(request, 'core/home.html')

def about(request):
    company_info = get_object_or_404(models.CompanyInfo)
    return render(request, "core/about.html", {"company_info": company_info})


def news_home(request):
    """Fetch the latest, trending, and all news for display."""
    top_news = models.News.objects.exclude(unique_id="").order_by('-created_at').first()  # Most recent news
    latest_news_list = models.News.objects.exclude(unique_id="").order_by('-created_at')[1:]  # Exclude top news
    trending_news = models.News.objects.exclude(unique_id="").order_by('-created_at')[:5]  # Top 5 trending news

    # Pagination for latest_news (7 per page)
    paginator = Paginator(latest_news_list, 6)
    page_number = request.GET.get('page')
    latest_news = paginator.get_page(page_number)

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

def team_view(request):
    """View to display all team members."""
    team_members = models.TeamMember.objects.all()
    return render(request, "core/team.html", {"team_members": team_members})

def contact(request):
    return render(request, 'core/contact.html')

def job_list_view(request):
    query = request.GET.get('q', '')
    lang = get_language()  # will return 'en', 'ja', or 'ne'

    # Dynamically pick the translated header field based on current language
    header_field = f'header_{lang}'
    
    job_list = models.Job.objects.all()

    if query:
        filter_kwargs = {f'{header_field}__icontains': query}
        job_list = job_list.filter(**filter_kwargs)

    job_list = job_list.order_by('-created_at')

    paginator = Paginator(job_list, 10)
    page = request.GET.get('page', 1)

    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        jobs = paginator.page(1)
    except EmptyPage:
        jobs = paginator.page(paginator.num_pages)

    return render(request, 'core/job_list.html', {'jobs': jobs, 'query': query})

def job_detail_view(request, unique_id):
    # Retrieve the job object based on the unique_id
    job = get_object_or_404(models.Job, unique_id=unique_id)
    
    
    context = {
        'job': job
    }
    return render(request, 'core/job_detail.html', context)


