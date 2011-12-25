# Create your views here.

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from models import InstaWallet
from forms import SendForm
from django.http import HttpResponseRedirect, HttpResponse
from django_bitcoin.utils import int2base64, base642int, generateuniquehash
from django_bitcoin import Wallet
import json
import os
import datetime

from django.utils.translation import ugettext as _

from django.contrib import messages

def home(request):
    # just generate a new wallet
    new_wallet=InstaWallet.objects.create(uuid=generateuniquehash(extradata=str(os.urandom(32))),\
        wallet=Wallet.objects.create())

    return HttpResponseRedirect(new_wallet.url())

def wallet(request, uuid):

    try:
        instawallet=InstaWallet.objects.get(uuid=uuid)
    except:
        return HttpResponseRedirect('/404')

    if request.method == 'POST': # If the form has been submitted...
        form = SendForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # check if 
            if len(form.cleaned_data["address_to"])>30 \
                and len(form.cleaned_data["address_to"])<37:
                try:
                    instawallet.wallet.send_to_address(form.cleaned_data["address_to"], form.cleaned_data["amount"])
                    messages.add_message(request, messages.SUCCESS, \
                        _(u"Transaction successfully sent to bitcoin address "+form.cleaned_data["address_to"]))
                except:
                    messages.add_message(request, messages.ERROR, sys.exc_info()[0])
            else:
                otherwallets=InstaWallet.objects.filter(uuid__startswith=form.cleaned_data["address_to"])
                if len(otherwallets)==1:
                    instawallet.wallet.send_to_wallet(otherwallets[0].wallet, form.cleaned_data["amount"])
                    messages.add_message(request, messages.SUCCESS, \
                        _(u"Transaction successfully sent to another instawallet "+form.cleaned_data["address_to"]))
                else:
                    messages.add_message(request, messages.ERROR, _(u"Address not an valid bitcoin address or wallet uuid not found."))
    else:
        form = SendForm() # An unbound form

    return render_to_response("instawallet.html", {
        "instawallet": instawallet,
        "form": form,
        }, context_instance=RequestContext(request))