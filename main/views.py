from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница сайта',
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'About',
        'content': 'Страница о нас!'
    }
    return render(request, 'main/about.html', context)