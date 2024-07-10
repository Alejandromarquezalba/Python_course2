from django import forms


class ClientForm(forms.Form):
    money = forms.CharField(max_length=100, required=True)
    product = forms.CharField(max_length=100, required=True)

class MarketForm(forms.Form):
    money = forms.CharField(max_length=100, required=True)
    client = forms.CharField(max_length=100, required=True)

class WorkerForm(forms.Form):
    pay = forms.CharField(max_length=100, required=True)
    hours = forms.IntegerField(required=True)





    