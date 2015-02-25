from django import forms
from measure.models import Measure

class TestForm(forms.ModelForm):
    class Meta:
        model = Measure
        fields = ('voltage', 'time', 'resolution',)


