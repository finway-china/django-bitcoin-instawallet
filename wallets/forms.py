# coding=utf8
# vim: ai ts=4 sts=4 et sw=4

from django import forms
from django.conf import settings
from django.db import models
from django.forms import ModelForm, Textarea, Select, ValidationError, TextInput
from django.utils.translation import ugettext as _
from decimal import Decimal
import datetime

class SendForm(forms.Form):
    address_to = forms.CharField(min_length=3, max_length=40)
    amount = forms.DecimalField(min_value=Decimal("0.0001"))
