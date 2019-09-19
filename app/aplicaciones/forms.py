from django.forms import forms

from .models import App

class AppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ['name', 'slug', 'descripcion', 'path_to_binary', 'user_id', 'app_type_id']
        labels = {
            'name': 'Nombre',
        }