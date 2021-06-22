from django.forms import ModelForm
from .models import *


class CreateArticle(ModelForm):
    class Meta:
        model = Article
        fields = ['title','slug','body','image']