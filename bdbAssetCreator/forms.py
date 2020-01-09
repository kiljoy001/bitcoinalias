from django import forms

class AliasForm(forms.Form):
    aliasString = forms.CharField(label='alias', max_length=150)
    bitcoinAddress = forms.CharField(label='address', max_length=35)