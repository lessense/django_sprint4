from django import forms
from django.contrib.auth import get_user_model

from .models import Comment, Post

User = get_user_model()


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = (
            'title', 'text', 'pub_date', 'category', 'location',
            'image', 'is_published',
        )
        widgets = {
            'pub_date': forms.DateTimeInput(
                format='%Y-%m-%dT%H:%M',
                attrs={'type': 'datetime-local'},
            ),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {'text': forms.Textarea(attrs={'rows': 4})}


class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
