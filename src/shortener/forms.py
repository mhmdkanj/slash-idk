from django import forms

from shortener.models import Shortener
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML
from crispy_forms.bootstrap import PrependedText

class ShortenerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_show_errors = True
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Row(
                Column('original', css_class='form-group col-lg-6'),
                css_class='form-row justify-content-center align-items-center mt-5'
            ),
            Row(
                Column(HTML('<i class="bi bi-arrow-down-circle-fill" style="font-size: 30px"></i>'), css_class='form-group col-lg-1 d-flex justify-content-center'),
                css_class='form-row justify-content-center align-items-center mx-3'
            ),
            Row(
                Column(PrependedText('shortened', "http://localhost:8000/"), css_class='form-group col-lg-3'),
                Column(HTML('<a class="btn btn-secondary" href="/suggest/name/" role="button">Suggest Name</a>'), css_class='form-group col-lg-2'),
                css_class='form-row justify-content-center mt-3'
            ),
            Row(
                Column(Submit('submit', '    Save    '), css_class='form-group col-lg-1 d-flex justify-content-center'),
                css_class='form-row justify-content-center align-items-center mt-3'
            )    
        )

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
