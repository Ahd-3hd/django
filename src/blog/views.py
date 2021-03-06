from django.shortcuts import render
from django.views.generic import ListView
from .models import Article
# Create your views here.

class ArticleListView(ListView):
    template_name = "articles/article_list.html"
    queryset = Article.objects.all()
