from django import forms
from .models import *
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','last_name','password','email')

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title','text','rasm','bolim')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('izoh',)


