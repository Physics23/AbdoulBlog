from django.shortcuts import render
from myblog.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)

#from . import views

#def frontpage(request):
#    posts = Post.objects.all()
#    return render(request, 'myblog/frontpage.html', {'posts':posts})

class PostListView(ListView):
    model = Post
    template_name = 'myblog/frontpage.html'
    context_object_name = 'posts'
    ordering = ['-date_added']

class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']


    def form_valid(self, form):
        form.instance.author =self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False




class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False



def about(request):
    return render(request, 'myblog/about.html')


def public(request):
    return render(request, 'myblog/public.html')


# Create your views here.
