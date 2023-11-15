from django import forms


class CreateSubtradeForm(forms.Form):
    text_subtrade = forms.CharField(label = "",max_length=100,widget=forms.Textarea(attrs={'rows': 50, 'cols': 400,'class': 'boites-container'}))