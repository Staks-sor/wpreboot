from django.db import models
from django.utils.text import slugify

from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.ImageField(upload_to='media/', verbose_name='Изображение', )
    title = models.CharField(max_length=500, verbose_name='Заголовок поста',)
    content = RichTextUploadingField(verbose_name='Содержимое поста',)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, unique=True)

    class Meta:
        verbose_name = 'Пост на сайте'
        verbose_name_plural = 'Посты на сайте'
        ordering = ['-id']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self): 
        return self.title

    def get_absolute_url(self, **kwargs):
        return f'/post/{self.id}/{self.slug}'
 