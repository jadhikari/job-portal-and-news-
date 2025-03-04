from django.shortcuts import render, redirect, get_object_or_404
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
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        purpose = request.POST.get('purpose')
        message = request.POST.get('message')

        # Compose email content
        email_subject = f"New Contact Message from {name} ({purpose})"
        email_body = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Address: {address}
        Purpose: {purpose}
        Message: {message}
        """

        # Send email (Replace with your actual email configuration)
        send_mail(
            subject=email_subject,
            message=email_body,
            from_email=email,
            recipient_list=['contact@enjapan.jp'],  # Change this to your official email
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect("contact")

    return render(request, "core/contact.html")
