from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('post/<int:pk>', PostDetail.as_view(), name='detail'),
    path('urls', UrlAll.as_view(), name='url'),
    path('yandex/turbo', YandexTurbo.as_view(), name='turbo')
]
