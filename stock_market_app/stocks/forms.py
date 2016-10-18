from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime

class HistoricalPricingForm(forms.Form):
    stock_symbol = forms.CharField(required=True,
                                   max_length=5,)

    start_date = forms.DateField(required=True,
                                 input_formats=['%Y-%m-%d'],
                                 widget=forms.SelectDateWidget(years=range(1980,2017)),
                                 initial=datetime.now())

    end_date = forms.DateField(required=True,
                               input_formats=['%Y-%m-%d'],
                               widget=forms.SelectDateWidget(years=range(1980,2017)),
                               initial=datetime.now())

    interval = forms.ChoiceField(choices=[('daily', 'daily'),
                                          ('weekly', 'weekly'),
                                          ('monthly', 'monthly')] )

    def clean(self):
        data = self.cleaned_data
        data['stock_symbol'] = data['stock_symbol'].upper()
        if data['start_date'] > data['end_date']:
            raise ValidationError('Start date should be before end date')
        if data['start_date'] == data['end_date']:
            raise ValidationError('Please select a range of more than one day')
        return data