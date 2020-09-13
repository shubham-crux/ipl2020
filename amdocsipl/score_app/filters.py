import django_filters
from .models import Wins
from django import forms


class WinsFilter(django_filters.FilterSet):

    class Meta:
        model = Wins
        fields = ['playerdetail', 'windate']
