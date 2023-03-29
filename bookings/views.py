from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
import datetime
from bookings.forms import BookingForm
from django.urls import reverse

# Create your views here.

def index(request):
    context = {}
    return render(request, 'bookings/index.html', context)


def book(request):
    
    if request.method == 'GET':
        
        today = timezone.now()
        day = request.GET.get('day', today.day)
        month = request.GET.get('month', today.month)
        year = request.GET.get('year', today.year)

        # Check if the date in the link is not old or malicious

        try:
            date = timezone.make_aware(datetime.datetime(year, month, day))
        except:
            date = today
        else:
            date = today if date < today else date

        # prepare a form with date as a starting point
        form = BookingForm(initial={'date': date})
        min_date = date.strftime('%Y-%m-%d')
        form.fields['date'].widget.attrs.update({'min': min_date})

        # send the form away!
        return render(request, 'bookings/book.html', {'form': form})
    
    else:

        return HttpResponseRedirect(reverse('bookings:book_page'))
