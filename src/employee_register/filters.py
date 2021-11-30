from django.db.models import fields
import django_filters
from django_filters import CharFilter
from .models import *

class OrderFilter(django_filters.FilterSet):
    fullname = CharFilter(field_name='fullname', lookup_expr='icontains')
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['email', 'mobile']

        
    def __init__(self, *args, **kwargs):
        super(OrderFilter, self).__init__(*args, **kwargs)
        self.filters['fullname'].label="სახელი, გვარი"
        self.filters['position'].label="თანამდებობა"
            
    