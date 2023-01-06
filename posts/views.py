from django.shortcuts import render, redirect
from posts.models import Post, Hashtag, Comment
from posts.forms import PostCreateForm, CommentCreateForm
from django.views.generic import ListView

# Create your views here.

PAGINATION_LIMIT = 3

def main_view(request):
    return render(request, 'layouts/index.html')

class PostsCBV(ListView):
    model = Post
    template_name = 'posts/posts.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'posts': kwargs['posts'],
            'user': kwargs['user'],
            'pages': kwargs['pages']
        }

    def get(self, request, **kwargs):
        hashtag_id = int(request.GET.get('hashtag_id', 0))
        text = request.GET.get('text')
        page = int(request.GET.get('page', 1))

        if hashtag_id:
            posts = self.model.objects.filter(hashtags__in=[hashtag_id])
        else:
            posts = self.model.objects.all()

        if text:
            posts = self.model.objects.filter(title__icontains=text)

        max_page = posts.__len__() / PAGINATION_LIMIT

        if round(max_page) < max_page:
            max_page = round(max_page)+1

        max_page = int(max_page)
        posts = posts[PAGINATION_LIMIT * (page-1): PAGINATION_LIMIT * page]

        return render(
            request,
            self.template_name,
            context=self.get_context_data(
                posts=posts,
                user=None if request.user.is_anonymous else request.user,
                pages=range(1, max_page+1)
            )
        )


# def posts_view(request):
#     if request.method == 'GET':
#         hashtag_id = int(request.GET.get('hashtag_id', 0))
#         text = request.GET.get('text')
#         page = int(request.GET.get('page', 1))
#
#         if hashtag_id:
#             posts = Post.objects.filter(hashtags__in=[hashtag_id])
#         else:
#             posts = Post.objects.all()
#
#         if text:
#             posts = Post.objects.filter(title__icontains=text)
#
#         max_page = posts.__len__() / PAGINATION_LIMIT
#
#         if round(max_page) < max_page:
#             max_page = round(max_page)+1
#
#         max_page = int(max_page)
#         posts = posts[PAGINATION_LIMIT * (page-1): PAGINATION_LIMIT * page]
#
#         return render(request, 'posts/posts.html', context={
#             'posts': posts,
#             'user': None if request.user.is_anonymous else request.user,
#             'pages': range(1, max_page+1)
#         })

def post_detail_view(request, id):
    if request.method == 'GET':
        post = Post.objects.get(id=id)

        context = {
            'post': post,
            'comments': post.comment_set.all(),
            'hashtags': post.hashtags.all(),
            'comment_form': CommentCreateForm
        }

        return render(request, 'posts/detail.html', context=context)

    if request.method == 'POST':
        post = Post.objects.get(id=id)
        form = CommentCreateForm(data=request.POST)

        if form.is_valid():
            Comment.objects.create(
                author=request.user,
                post_id=id,
                text=form.cleaned_data.get('text')
            )
            return redirect(f'/posts/{id}')
        else:
            return render(request, 'posts/detail.html', context={
                'post': post,
                'comments': post.comment_set.all(),
                'hashtags': post.hashtags.all(),
                'comment_form': form
            })

def hashtags_view(request):
    if request.method == 'GET':
        hashtags = Hashtag.objects.all()

        context = {
            'hashtags': hashtags
        }

        return render(request, 'hashtags/index.html', context=context)

def post_create_view(request):
    if request.method == 'GET':
        return render(request, 'posts/create.html', context={
            'form': PostCreateForm
        })

    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)

        if form.is_valid():
            Post.objects.create(
                image=form.cleaned_data.get('image'),
                author=request.user,
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data.get('rate', 0)
            )
            return redirect('/posts/')
        else:
            return render(request, 'posts/create.html', context={
                'form': form
            })

