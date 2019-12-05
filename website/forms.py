from django import forms
# https://docs.djangoproject.com/en/2.2/ref/forms/fields/#datetimefield


class AuctionForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    picture = forms.ImageField()
    starting = forms.DecimalField(
        label='Starting Price', decimal_places=2, max_digits=10)
    auctionEnd = forms.DateTimeField(label='when does the auction end',
                                     widget=forms.TextInput(attrs={'type': 'datetime-local'}))
    length = forms.DecimalField(
        label='Length in centimetres', decimal_places=2, max_digits=10)
    width = forms.DecimalField(
        label='Width in centimetres', decimal_places=2, max_digits=10)
    height = forms.DecimalField(
        label='Height in centimetres', decimal_places=2, max_digits=10)
    weight = forms.DecimalField(
        label='Weight in Kilograms', decimal_places=2, max_digits=10)
