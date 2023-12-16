from django import forms
from .models import Items,Bids,Search

class ItemsForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['title','bid','image']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ["bid"]
        labels = {
            "bid": "Your Bid",
        }
class SearchForm(forms.ModelForm):
    class Meta:
        model=Search
        fields="__all__"

    title = forms.CharField(required=False)

class DeleteForm(forms.ModelForm):
    class Meta:
        model=Items
        fields=['title']