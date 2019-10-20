from django.shortcuts import render, get_object_or_404
import markdown

from blog.models import Post


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={
        'post_list': post_list,
    })


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      # 包含 缩写、表格等常用扩展
                                      'markdown.extensions.extra',
                                      # 语法高亮扩展
                                      'markdown.extensions.codehilite',
                                      # 允许自动生成目录
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/detail.html', context={'post': post})
