from django import forms
from . models import Posts
class Postsform(forms.ModelForm):
    class Meta:
        model = Posts
        fields = "__all__"