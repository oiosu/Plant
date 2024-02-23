from django import forms
from .models import Article
from django_summernote.widgets import SummernoteWidget

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content"]
        widgets = {
            'content' : SummernoteWidget(),
        }

