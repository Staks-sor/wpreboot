from django.contrib.sitemaps import Sitemap
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from yaturbo import YandexTurboFeed

from blog.models import Post


class Index(ListView):
    template_name = 'index.html'

    def get(self, request):
        slider = Post.objects.order_by('-date').order_by("?")[0:4]
        post = Post.objects.order_by('-date')[0:6]

        context = {
            'slider': slider,
            'post': post
        }
        return render(request, self.template_name, context)


class PostDetail(DetailView):
    template_name = 'Template/post-card.html'

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        share = Post.objects.order_by('-date').order_by("?")[0:8]
        share_left = Post.objects.order_by('-date').order_by("?")[0:5]
        context = {
            'post': post,
            'share': share,
            'share_left': share_left,
        }
        return render(request, self.template_name, context)


class UrlAll(ListView):
    template_name = 'Template/sitemap.html'
    model = Post
    context_object_name = 'post'
    paginate_by = 1000


class YandexTurbo(ListView):
    template_name = 'turbo.xml'
    model = Post
    context_object_name = 'turbo'
    paginate_by = 1000
