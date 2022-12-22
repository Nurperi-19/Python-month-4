from django.shortcuts import render
from posts.models import Post, Hashtag
# Create your views here.

def main_view(request):
    return render(request, 'layouts/index.html')

def posts_view(request):
    if request.method == 'GET':
        hashtag_id = int(request.GET.get('hashtag_id', 0))

        if hashtag_id:
            posts = Post.objects.filter(hashtags__in=[hashtag_id])
        else:
            posts = Post.objects.all()

        return render(request, 'posts/posts.html', context={
            'posts': posts
        })

def post_detail_view(request, id):
    if request.method == 'GET':
        post = Post.objects.get(id=id)

        context = {
            'post': post,
            'comments': post.comment_set.all(),
            'hashtags': post.hashtags.all()
        }

        return render(request, 'posts/detail.html', context=context)

def hashtags_view(request):
    if request.method == 'GET':
        hashtags = Hashtag.objects.all()

        context = {
            'hashtags': hashtags
        }

        return render(request, 'hashtags/index.html', context=context)

