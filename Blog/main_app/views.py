from django.shortcuts import render, redirect
from .models import Post, Comment
from django.http import HttpRequest

# Create your views here.

def home(request):
    posts = Post.objects.filter(is_published=True)
    return render(request, 'main_app/home.html', {'posts': posts})


def add_post(request:HttpRequest):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        is_published = request.POST["is_published"]
        publish_date = request.POST["publish_date"]
        new_post = Post(Title=title, Content=content, is_published=is_published, publish_date=publish_date)
        new_post.save()
        return redirect('main_app:home') 
    else: 
        return render(request, 'main_app/add_post.html')


def post_details(request:HttpRequest, post_id):
    try:
        post = Post.objects.get(id=post_id)
        comments = Comment.objects.filter(post=post_id)
    except:
        return render(request, 'main_app/no_post.html')
    return render(request, 'main_app/post_details.html', {"post": post,"comments": comments})


def update_post(request:HttpRequest, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        post.Title = request.POST['title']
        post.Content = request.POST['content']
        post.is_published = request.POST["is_published"]
        post.publish_date = request.POST["publish_date"]
        post.save()
        return redirect("main_app:post_details", post_id = post.id)
    else:
        return render(request, 'main_app/update_post.html', {"post" : post})
    

def delete_post(request:HttpRequest, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect("main_app:home")


def search(request:HttpRequest):
    search_phrase = request.GET.get("search", "")
    post = Post.objects.filter(Title__contains=search_phrase)
    return render(request, "main_app/search.html", {"posts" : post})


def add_comment(request:HttpRequest, post_id):
    if request.method == "POST":
        post_object = Post.objects.get(id=post_id)
        name = request.POST['name']
        content = request.POST['content']
        new_comment = Comment(post=post_object, name=name, content=content)
        new_comment.save()
    return redirect("main_app:post_details", post_id=post_id)