from django.forms import ModelForm
from .models import *
class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['model', 'brand', 'wheel']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['model'].widget.attrs['data-lead-id'] = self.instance.model
        self.fields['brand'].widget.attrs['data-lead-id'] = self.instance.brand
        self.fields['wheel'].widget.attrs['data-lead-id'] = self.instance.wheel
        self.fields['model'].widget.attrs['disabled'] = 'disabled'
        self.fields['brand'].widget.attrs['disabled'] = 'disabled'
        self.fields['wheel'].widget.attrs['disabled'] = 'disabled'