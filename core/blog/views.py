from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)

from django.views.generic import ListView,DetailView,FormView,CreateView,UpdateView,DeleteView
from .models import *
from .forms import PostForm


class IndexView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()[:5]
        return context
    


class PostListView(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    permission_required = "blog.view_post"
    model = Post
    template_name = 'blog/post_list.html' 
    context_object_name = 'posts'


class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = "blog/post_detail.html"


    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
    

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    


class PostEditView(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = '/blog/post/'