from django.contrib.sitemaps import Sitemap
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.db.utils import IntegrityError
from django.core.files.base import ContentFile

from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

from yaturbo import YandexTurboFeed

from blog.models import Post
from blog.serializers import PostSerializer

import base64


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



class ParceObjects(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser, FileUploadParser]

    def perform_create(self, serializer):
        if serializer.is_valid(raise_exception=True):

            serializer.save(image=self.request.data.get('image'),)
            return Response(serializer.data, status=201)
        return Response({'data': 'invalid data'}, status=400)

