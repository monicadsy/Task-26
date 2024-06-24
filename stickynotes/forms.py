from django import forms
from .models import Stickynote


class StickynoteForm(forms.ModelForm):
    """
    Form for creating and updating Note objects.
    Fields:
    - title: Charfield for the post title.
    - content: TextField for the post content
    Meta class:
    - Defines the model to use Note and the fields to include in the form.
    """
    class Meta:
        model = Stickynote
        fields = ['name', 'sets', 'description', 'creator']
