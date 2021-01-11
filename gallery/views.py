from django.shortcuts import render
from .models import Image
import datetime as dt
from django.http  import HttpResponse,Http404

# Create your views here.

def welcome(request):
   title= 'Welcome  to my Gallerie'
   images = Image.objects.all()
   return render(request, 'gallery/home.html', {'title' :title,'images':images})


def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_articles = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message}) 
# def article(request,article_id):
#     try:
#         article = Article.objects.get(id = article_id)
#     except DoesNotExist:
#         raise Http404()
#     return render(request,"all-news/article.html", {"article":article})