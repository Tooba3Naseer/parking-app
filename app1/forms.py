from django import forms
from .models import parkingSlots

class parkingForm(forms.ModelForm):
    class Meta:
        model = parkingSlots
        fields = ('slot_no','car_no','limit') 