from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST

from ..forms import CommentForm
from ..models import Post

User = get_user_model()

__all__ = (
    'comment_create',
    'comment_modify',
    'comment_delete',
)


@require_POST
@login_required
def comment_create(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('post:post_detail', post_pk=post.pk)


def comment_modify(request, post_pk):
    # 수정
    pass


def comment_delete(request, post_pk, comment_pk):
    # POST요청을 받아 Comment객체를 delete, 이후 post_detail페이지로 redirect
    pass
