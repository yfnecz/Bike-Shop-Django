from .models import Order
from django.forms import ModelForm


class OrderForm(ModelForm):
        class Meta:
            model = Order
            exclude = ['bike', 'status']
            labels = {
                "name": "your name",
                "surname": "your surname",
                "phone_number": "your phone number"
            }
