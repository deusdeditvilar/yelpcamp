import django_filters
from django.forms import Select
from .models import Campground
from django import forms

class CampgroundFilter(django_filters.FilterSet):

    name = django_filters.filterset.CharFilter(lookup_expr='icontains', label="Name",widget=forms.TextInput(attrs={'class': 'uk-input uk-form-width-medium','placeholder':"Search for camps"}))

    class Meta:
        model = Campground
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(CampgroundFilter, self).__init__(*args, **kwargs)
