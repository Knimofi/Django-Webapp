from django.shortcuts import render
from django.http import HttpResponse

posts = [

    {
        'title': 'Melbourne',
        'author': 'Karla',
        'post_date': 'March 2019',
        'content': 'Grampians, St.Kilda, Flinders'
    },
    {
        'title': 'Perth',
        'author': 'Luai',
        'post_date': 'April 2019',
        'content': 'OBB, Cottesloe, Freementle, Rottnest Island'
    }
]


# Create your views here.
def home(request):
    context = {
        'posts': posts
    };
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', { 'title': 'About Page' })
