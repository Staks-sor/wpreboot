from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    # image = Base64ImageField()
    class Meta:
        model = Post
        fields = '__all__'

    # def create(self, validated_data):
    #     image = validated_data.pop('image')
    #     title = validated_data.pop('title')
    #     content = validated_data.pop('content')
    #     return Post.objects.create(image=image, title=title, content=content)
