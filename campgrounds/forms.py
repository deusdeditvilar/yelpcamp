from django import forms
from .models import *

class CampgroundForm(forms.ModelForm):
    name = forms.CharField(label='Camp Name',widget=forms.TextInput(attrs={'class': 'yelp-input','placeholder':'Seven Sisters Waterfall'}),required=True)
    price = forms.CharField(label='Price', widget=forms.TextInput(attrs={'class': 'yelp-input','placeholder':'$149'}),required=True)
    image = forms.CharField(label='Image URL', widget=forms.TextInput(attrs={'class': 'yelp-input','placeholder':'https://i.pinimg.com/originals/c1/be/5c/c1be5c01ff0b6168a5d16e96e0fce8de.jpg'}),required=True)
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'yelp-input','placeholder':"The Seven Sisters is the 39th tallest waterfall in Norway. The 410-metre tall waterfall consists of seven separate streams,and the tallest of the seven has a free fall that measures 250 metres. The waterfall is located along the Geirangerfjorden in Stranda Municipality in Møre og Romsdal county, Norway."}))
    address = forms.CharField(label='Description',widget=forms.TextInput(attrs={'class':'yelp-input','placeholder':'Seve Sisters Waterfall'}))

    class Meta:
        model = Campground
        fields = ('name','price','image','description','address',)

class CommentForm(forms.ModelForm):
    
    comment = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'yelp-input','maxlength':300,'placeholder':"This was probably the best camp i've visited this past year, definitely recommend visiting any time soon."}))

    class Meta:
        model = Comment
        fields = ("comment",)
