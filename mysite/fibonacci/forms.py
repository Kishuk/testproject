from django import forms

class NameForm(forms.Form):
    number = forms.IntegerField()