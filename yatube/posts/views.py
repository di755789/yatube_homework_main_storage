from django.shortcuts import get_object_or_404, render
from .models import Post, Group
POST_COUNT = 10


def index(request):
    template = 'posts/group_list.html'
    posts = Post.objects.order_by('-pub_date')[:POST_COUNT]
    context = {
        'posts': posts,
        'title': "Последние обновления на сайте",
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:POST_COUNT]
    context = {
        'group': group,
        'posts': posts,
        'title': "Все записи группы",
    }
    return render(request, template, context)
