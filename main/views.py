from unicodedata import category
from django.shortcuts import render

from goods.models import Category

# Create your views here.
def index(request):

    categories = Category.objects.all()

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
        'categories': categories,
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас!',
        'text_on_page': 'Какое-то описание магазина - бла, бла, бла!'
    }
    return render(request, 'main/about.html', context)