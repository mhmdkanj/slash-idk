from django import forms

from shortener.models import Shortener

class ShortenerForm(forms.ModelForm):
    shortened = forms.SlugField(
        max_length=50,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "idk",
        })
    )

    original = forms.URLField(
        max_length=400,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "http://www.some.thing/very/long",
        })
    )

    class Meta:
        model = Shortener
        fields = [
            'shortened',
            'original'
        ]

    def clean_shortened(self, *args, **kwargs):
        shortened = self.cleaned_data.get('shortened')
        if Shortener.objects.filter(shortened=shortened):
            raise forms.ValidationError("This name is already taken.")
        return shortened
