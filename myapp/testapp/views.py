from django.shortcuts import render, redirect
from .models import Post, Comment, Like
from django.contrib.auth.decorators import login_required

@login_required
def post_list(request):
    posts = Post.objects.all()
    print('posts', posts)
    return render(request, 'testapp/post_list.html', {'posts': posts})

@login_required
def add_post(request):
    if request.method == 'POST':
        content = request.POST['content']
        post = Post.objects.create(user=request.user, content=content)
        return redirect('post_list')

@login_required
def add_comment(request, post_id):
    if request.method == 'POST':
        text = request.POST['text']
        post = Post.objects.get(pk=post_id)
        comment = Comment.objects.create(post=post, user=request.user, text=text)
        return redirect('post_list')

@login_required
def like_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        like.delete()
    return redirect('post_list')
