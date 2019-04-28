from django.shortcuts import render
from .models import Post

def index(request):
    return render(request, 'mainApp/main.html')

def news(request):
    return render(request, 'mainApp/news.html')


def post_list(request):
    post = Post.objects.filter(moder=True)
    return render(request, "news/post_list.html", {"posts": post})