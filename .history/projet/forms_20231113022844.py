from django import forms


class CreateSubtradeForm(forms.Form):
    text_subtrade = forms.CharField(label = "Text", max_length=100)