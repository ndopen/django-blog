from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    '''Post share Email form'''
    name = forms.CharField(max_length=250)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    '''Comment Forms'''
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class SerachForm(forms.Form):
    '''搜索表单'''
    query = forms.CharField()