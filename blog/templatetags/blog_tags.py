from ..models import Post, Category, Tag
from comments.models import Comment
from django import template
from django.db.models.aggregates import Count


register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def get_recent_posts_for_index(num=3):
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)


@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)


@register.simple_tag
def get_recent_comments(num=6):
    return Comment.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def get_most_view_post(num=3):
    return Post.objects.all().order_by('-views')[:num]
