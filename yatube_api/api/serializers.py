from posts.models import Comment, Group, Post
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description', 'posts')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    group = serializers.SlugRelatedField(
        read_only=True, slug_field='title'
    )

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group')
