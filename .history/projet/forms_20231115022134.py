from django import forms


class CreateSubtradeForm(forms.Form):
    text_subtrade = forms.CharField(label = "Text", max_length=100,widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))