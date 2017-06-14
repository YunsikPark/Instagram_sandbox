from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from member.models import User
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post/post_list.html', context)


def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    template = loader.get_template('post/post_detail.html')
    context = {
        'post' : post,
    }
    rendered_string = template.render(context=context, request=request)
    return HttpResponse(rendered_string)

def post_create(request):
    # POST요청을 받아 Post객체를 생성 후 post_list페이지로 redirect
    pass


def post_modify(request, post_pk):
    # 수정
    pass


def post_delete(request, post_pk):
    # post_pk에 해당하는 Post에 대한 delete요청만을 받음
    # 처리완료후에는 post_list페이지로 redirect
    pass


def comment_create(request, post_pk):
    # POST요청을 받아 Comment객체를 생성 후 post_detail페이지로 redirect
    pass


def comment_modify(request, post_pk):
    # 수정
    pass


def comment_delete(request, post_pk, comment_pk):
    # POST요청을 받아 Comment객체를 delete, 이후 post_detail페이지로 redirect
    pass
