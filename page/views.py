from django.shortcuts import render, redirect, get_object_or_404
from .models import Post


# Create your views here.

def home(request):
    return render(request, 'home.html')


def map_view(request):
    posts = Post.objects.all()
    return render(request, 'map.html', {'posts': posts})


def post_save(request):
    if request.method == 'POST':
        post_id = request.POST['post_id']
        post = Post()
        if post_id is not None:
            post = get_object_or_404(Post, pk=int(post_id))
        post.action = request.POST['action']
        post.date = request.POST['date']
        post.cat_name = request.POST['cat_name']
        image = request.POST['image']
        post.lat = request.POST['lat']
        post.lng = request.POST['lng']
        if image is not None:
            post.image = request.POST['image']
        post.save()
        return redirect('home')
