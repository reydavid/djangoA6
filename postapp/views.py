from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

# Create your views here.

def index(request):
    context = {
        "allPosts" : Post.objects.all()
    }
    return render(request, 'postapp/index.html', context)

def addPost(request):
    if request.method == "POST":
        user_post = request.POST['post']
        post = Post.objects.create(post = user_post)
    
    return redirect('/')

def editPost(request,id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "GET":
        context = {
            "post": post
        }
        return render(request, "postapp/update.html",context)
    else:
        post.post = request.POST["post"]
        post.save()

    return redirect('/')

def removePost(request,id):
        post = Post.objects.get(id = id).delete()
    
        return redirect('/')
