from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import AliasForm
from bitcoin_alias.asset_handling.create_user import User
from bitcoin_alias.asset_handling.asset_template import Asset

def get_name(request):
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
            return HttpResponseRedirect('/')
    



