from django.core.validators import MinValueValidator, MaxValueValidator
from django import forms

class GenerateRandomUserForm(forms.Form):
    total = forms.IntegerField(
        validators=[
            MinValueValidator(50),
            MaxValueValidator(500)
        ]
    )