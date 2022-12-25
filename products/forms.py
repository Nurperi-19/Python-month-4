from django import forms


class ProductCreateForm(forms.Form):
    category = forms.CharField(max_length=255)
    name = forms.CharField(max_length=255)
    color = forms.CharField()
    description = forms.CharField(widget=forms.Textarea())
    price = forms.FloatField()

class ReviewCreateForm(forms.Form):
    text = forms.CharField(min_length=2, label='Leave a review')
