from django.shortcuts import render
from .models import News

# Create your views here.
def news(request):
  news_ordered = News.objects.all().order_by("-date")  # '-' means sort descending.
  return render(request, "news.html", {"news_ordered": news_ordered})
