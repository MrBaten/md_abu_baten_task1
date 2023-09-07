from django import forms
from .models import TradeData

class TradeDataForm(forms.ModelForm):
    class Meta:
        model = TradeData
        fields = '__all__'