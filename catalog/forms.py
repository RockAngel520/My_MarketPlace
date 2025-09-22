from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.models import Product

BANNED_WORDS = ('казино',
                'криптовалюта',
                'крипта',
                'биржа',
                'дешево',
                'бесплатно',
                'обман',
                'полиция',
                'радар')


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        else:
            return price

    def clean_name(self):
        name = self.cleaned_data['name']
        for banned_word in BANNED_WORDS:
            if banned_word in name.lower():
                raise ValidationError("Не используйте запрещенные слова")
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        for banned_word in BANNED_WORDS:
            if banned_word in description.lower():
                raise ValidationError("Не используйте запрещенные слова")
        return description
