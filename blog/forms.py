from django import forms

from .models import Post

#form name 
class PostForm(forms.ModelForm):

    class Meta:
        #모델 정의 
        model = Post
        
        fields = ('title', 'text',)