from django import forms

from .models import (Apprenant, Formateur, Hobbies)

class HobbiesForm(forms.ModelForm):
    
    class Meta:
        model = Hobbies
        fields = ('type_hobby', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self):
        type_hobby = self.cleaned_data['type_hobby']
        description = self.cleaned_data['description']
        hobby = Hobbies.objects.create(
            type_hobby = type_hobby,
            description = description
        )