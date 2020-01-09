from django import forms
from bitcoin_alias.asset_handling.create_user import User
from bitcoin_alias.asset_handling.asset_template import Asset
from django.http import HttpResponseRedirect, HttpResponse

class AliasForm(forms.Form):
    aliasString = forms.CharField(label='alias', max_length=150)
    bitcoinAddress = forms.CharField(label='address', max_length=35)

    def get_data(self, request):
        if request.method == 'POST':
            form = AliasForm(request.POST)
            if form.is_valid():
                cleaned_alias = form.cleaned_data['aliasString']
                cleaned_address = form.cleaned_data['bitcoinAddress']
                bdb_user = User()
                bdb_user.generate_keys()
                bdb_user.set_bitcoin_address_and_alias(cleaned_alias, cleaned_address)
                bdb_asset = Asset(bdb_user)
                transaction_id = bdb_asset.create_asset()
                transaction_id.save()

                #return back to page
                return HttpResponse(),HttpResponseRedirect('')