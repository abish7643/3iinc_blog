from django.shortcuts import render
from .models import Post

#from django.http import HttpResponse
# Create your views here.

#--------------Dummy data

# posts=[
#     {
#         'author': 'Abish',
#         'title': 'Test Post 1',
#         'content': 'lorem lepsum',
#         'date_posted': '3 August 2019',
#         'image': 'download.jpeg'
#     },
#     {
#         'author': 'Adith',
#         'title': 'Test Post 2',
#         'content': 'lorem lepsum 123',
#         'date_posted': '4 August 2019',
#         'image': 'download.jpeg'
#     },
#     
# ]

#----------------------------

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})