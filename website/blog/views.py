from.models import Post

from django.shortcuts import render, redirect

from .models import Post, PostForm
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

def form_post(request):
    if request.method == 'POST':
        data = PostForm(request.POST)

        if data.is_valid():
            in_data = Post(**data.cleaned_data)
            in_data.save()

    form = PostForm()

    return render(request, 'blog/forms.html', {'form': form})
