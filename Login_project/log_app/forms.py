from django import forms
from django.core.validators import MinValueValidator

GENDER=[('Male','Male'),('Female','Female')]

class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=100,
        required=True,
    )
    name = forms.CharField(
        max_length=100,
        required=True,
    )
    age = forms.IntegerField(
        validators=[MinValueValidator(18)]
    
    )
    gender=forms.CharField(
        label='Gender',
        widget=forms.RadioSelect(choices=GENDER)

    )
    
    
    