from django.shortcuts import render
from.models import Post
# Create your views here. 
def index(request):
    db = Post.objects.all()
    context = {
         'title': 'Blog',
         'Heading': 'Blog',
         'subheading' : 'postingan',
         'post': db,
    }
    return render(request,'blog\wiw.html' , context )
