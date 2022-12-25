from django import forms


class PostCreateForm(forms.Form):
    title = forms.CharField(max_length=20)
    description = forms.CharField(widget=forms.Textarea())
    rate = forms.FloatField(max_value=10)

class CommentCreateForm(forms.Form):
    text = forms.CharField(min_length=3, label='Add your comment')
