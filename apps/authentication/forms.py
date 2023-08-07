from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User

from authentication.validators import *

import re


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email', 'cpf', 'cep', 'is_voluntary', 'is_supporter', 'birthdate',
            'address', 'complement', 'password'
        ]

    password = forms.CharField(
        validators=[special_characters, uppercase_letters, lowercase_letters, number_validator]
    )

    cpf = forms.CharField(max_length=14)
    cep = forms.CharField(max_length=9)
    address = forms.CharField(max_length=64)

    def clean_cpf(self):
        
        return self._remove_characters('cpf')
    
    def clean_cep(self):

        return self._remove_characters('cep')

    def clean(self):

        cleaned_data = super().clean()
        cleaned_data['cpf'] = self.clean_cpf()
        cleaned_data['cep'] = self.clean_cep()

        return cleaned_data
    
    def save(self, commit=True):

        instance = super().save(commit=False)
        instance.cpf = self.cleaned_data.get('cpf')
        instance.cep = self.cleaned_data.get('cep')

        password = self.cleaned_data['password']
        if password:
            instance.set_password(password)

        if commit:
            instance.save()

        return instance
    
    def _remove_characters(self, key: str):

        return re.sub(r'[^0-9]', '', self.data[key])
    

class UserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):

        model = User


class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):

        model = User

