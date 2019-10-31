from django import forms

class UserLogin(forms.Form):
    login = forms.CharField(
        label="podaj login",
        max_length=20,
        widget=forms.TextInput()
    )