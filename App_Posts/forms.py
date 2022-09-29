from django import forms
from App_Posts.models import Post

######### Post Form #########
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('image', 'caption')