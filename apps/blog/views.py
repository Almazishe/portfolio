from django.shortcuts import render, redirect
from django.views.generic import View, DetailView

from .models import Post
from .forms import CommentForm, PostForm



class HomeView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_at')
        return render(request, 'home.html', {
            'posts': posts
        })


class LeaveComment(View):
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect(form.instance.post.get_absolute_url())

class PostDetail(DetailView):
    model = Post
    slug_url_kwarg = 'slug'
    template_name = 'posts/post_detail.html'

class CreatePostView(View):
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST, files=request.FILES)
        print(request.POST)
        if form.is_valid():
            post = form.save()
            post.owner = request.user
            post.save()
        else:
            print(form.errors)
            return redirect('home')
        return redirect(form.instance.get_absolute_url())