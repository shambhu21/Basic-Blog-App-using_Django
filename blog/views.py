from django.shortcuts import render

posts = [
    {
        'author': 'Shubham',
        'title': 'Blog Post 1',
        'content': 'First post comment',
        'date_posted': 'August 27th, 2018'
    },
    {
        'author': 'Sandesh',
        'title': 'Blog Post 2',
        'content': '2nd  post comment',
        'date_posted': 'Sept 27th, 2018'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})