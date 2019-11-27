from django import forms

class AuctionForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget = forms.Textarea)
    picture = forms.ImageField()