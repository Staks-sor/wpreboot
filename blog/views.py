import os

from django.core.files.base import ContentFile, File
from django.core.files.temp import NamedTemporaryFile
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from randomfilestorage.storage import RandomFileSystemStorage
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from blog.models import Post
import urllib.request as urllib2

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

random_storage = RandomFileSystemStorage(location='/media/')

class ParceObjects(APIView):
    
    def post(self, request):
        try:
            form = request.data
            title = form['title']
            img_temp = NamedTemporaryFile()
            img_temp.write(urllib2.urlopen(form['image']).read())
            img_temp.flush()
            Post.objects.create(title=form['title'], content=form['content'], image=File(img_temp, name=f'{title}.jpg'))
            return Response('', status=status.HTTP_201_CREATED)
        except ValueError or OSError:
            form = request.data
            Post.objects.create(title=form['title'], content=form['content'])
            return Response('', status=status.HTTP_201_CREATED)


