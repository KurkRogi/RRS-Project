from bookings.models import Booking, Table
from django import forms
import datetime


class BookingForm(forms.ModelForm):
    # change the widget of the date field.
    date = forms.DateField()
    date.label = 'Date'
    date.widget = forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})

    time = forms.ChoiceField()
    time.label = 'Time'
    time.choices = Booking.BOOKING_TIMES
    time.widget.attrs.update({'class': 'form-control'})

    tables = forms.ModelMultipleChoiceField(queryset = Table.objects.all())
    tables.label = 'Tables'
    tables.widget = forms.SelectMultiple()
    tables.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Booking
        fields = ('date', 'time', 'tables')
