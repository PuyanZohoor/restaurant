from django import forms
from .models import Tables

class TableForm(forms.ModelForm):
    TOTAL_PERSONS = (
        ('Two', '2'),
        ('Three', '3'),
        ('Four', '4'),
        ('Five', '5'),
    )
    name = forms.CharField(max_length=256)
    phone_number = forms.IntegerField()
    email = forms.EmailField()
    persons = forms.ChoiceField(choices=TOTAL_PERSONS)
    date = forms.DateField()
    class Meta:
        model = Tables
        fields = ['is_reserved']
