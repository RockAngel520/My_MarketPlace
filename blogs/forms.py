from django.forms import ModelForm

from blogs.models import Blog
from catalog.forms import StyleFormMixin


class BlogForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Blog
        exclude = ("views_count",)
