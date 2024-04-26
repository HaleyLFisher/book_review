from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import Review

class ReviewForm(forms.ModelForm):
    stars = forms.ChoiceField(
        choices=Review.rate_choices,
        widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = Review
        fields = ['title', 'content', 'stars', 'user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'title',
            'content',
            'stars',
            'user',
            Submit('submit', 'Submit', css_class='btn-success')
        )