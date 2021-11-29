from django import forms
from . import models


class SearchForm(forms.Form):
    name = forms.CharField(required=False)
    upjong = forms.CharField(required=False)
    rating_average = forms.DecimalField(required=False)
    address = forms.CharField(required=False)
