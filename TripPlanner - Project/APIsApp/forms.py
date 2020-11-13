from django import forms

class CoordinatesForm(forms.Form):
    longitude_start = forms.FloatField(label='longitude_start')
    latitude_start = forms.FloatField(label='latitude_start')
    longitude_end = forms.FloatField(label='longitude_end')
    latitude_end = forms.FloatField(label='latitude_end')