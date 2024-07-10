from django import forms


class classForm (forms.Form):
    money = forms.CharField(max_length=100, required=True)
    product = forms.IntegerField(required=True)

class classForm2 (forms.Form):
    money = forms.CharField(max_length=100, required=True)
    client = forms.IntegerField(required=True)

class classForm3 (forms.Form):
    pay = forms.CharField(max_length=100, required=True)
    hours = forms.IntegerField(required=True)





    