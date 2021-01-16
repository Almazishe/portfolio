from django import forms

from .models import PostComment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = '__all__'

class PostForm(forms.ModelForm):
    image = forms.ImageField()
    class Meta:
        model = Post
        fields = (
            'title', 'image', 'text',
        )