from bookings.models import Booking, Table
from django import forms
import datetime


class UserBookingForm(forms.ModelForm):
    # change the widget of the date field.
    
    class Meta:
        model = Booking
        fields = ('date', 'time', 'tables')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.Select(choices = Booking.BOOKING_TIMES, attrs={'class': 'form-control'}),
            'tables': forms.SelectMultiple(attrs={'class': 'form-control'})
        }


class AdminBookingForm(forms.ModelForm):
    # change the widget of the date field.
    
    class Meta:
        model = Booking
        fields = ('name', 'date', 'time', 'tables')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.Select(choices = Booking.BOOKING_TIMES, attrs={'class': 'form-control'}),
            'tables': forms.SelectMultiple(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(AdminBookingForm, self).__init__(*args, **kwargs)
        # enforce class='form-control' on name for Bootstrap
        self.fields['name'].widget.attrs={'class': 'form-control'}
        # for name in self.fields.keys():
        #     self.fields[name].widget.attrs.update({
        #         'class': 'form-control',
        #     })