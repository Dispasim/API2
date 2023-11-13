from django import forms


class CreateSubtradeForm(forms.Form):
    text_subtrade = forms.TextField(label = "Text")