from django.db import models


class Post(models.Model):
    image = models.ImageField(upload_to='media/', verbose_name='Изображение',  blank=True)
    title = models.CharField(max_length=500, verbose_name='Заголовок поста')
    content = models.TextField(verbose_name='Содержимое поста')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Пост на сайте'
        verbose_name_plural = 'Посты на сайте'
        ordering = ['-id']

    def __str__(self): 
        return self.title

    def get_absolute_url(self):
        return f'/post/{self.pk}'
