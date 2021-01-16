from django import template
from django.utils.safestring import mark_safe
from django.shortcuts import get_object_or_404

register = template.Library()

from apps.blog.models import Post, PostComment


@register.inclusion_tag("tags/comments.html")
def get_comments(count=None, post_id=None, user=None):

    post = get_object_or_404(Post, uuid=post_id)
    comments = post.comments.filter(parent=None)
    if count:
        comments = comments[:count]
    return {
        'comments': comments,
        'post': post,
        'user': user,
        'count': count
    }

@register.inclusion_tag("tags/subcomments.html")
def get_subcomments(count=None, comment_id=None):
    comment = get_object_or_404(PostComment, uuid=comment_id)
    subcomments = comment.children.all()
    if count:
        subcomments = subcomments[:count]
    return {
        "subcomments": subcomments,
    }