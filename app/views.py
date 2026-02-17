from django.shortcuts import render, get_object_or_404
from .models import News

#def home(request):
#    news = News.objects.all().order_by('-id')
#    return render(request, 'home.html', {'news': news})


def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    return render(request, 'detail.html', {'news': news})


from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def category(request):
    return render(request, 'category.html')

def single(request):
    return render(request, 'single.html')

def contact(request):
    return render(request, 'contact.html')
