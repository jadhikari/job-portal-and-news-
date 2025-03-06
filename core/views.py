
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')


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
    job_list = models.Job.objects.all().order_by('-created_at')  # Retrieve all jobs, ordered by creation date
    paginator = Paginator(job_list, 10)  # Display 10 jobs per page

    page = request.GET.get('page', 1)
    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        jobs = paginator.page(1)
    except EmptyPage:
        jobs = paginator.page(paginator.num_pages)

    return render(request, 'core/job_list.html', {'jobs': jobs})

def job_detail_view(request, unique_id):
    # Retrieve the job object based on the unique_id
    job = get_object_or_404(models.Job, unique_id=unique_id)
    
    
    context = {
        'job': job
    }
    return render(request, 'core/job_detail.html', context)


