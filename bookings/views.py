from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.utils import timezone
import datetime
from bookings.forms import UserBookingForm, AdminBookingForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Table, Booking
# from django.core import serializers

# Create your views here.

def index(request):
    context = {}
    return render(request, 'bookings/index.html', context)

def check_available_tables(request):
    date = request.GET.get('date')
    time = request.GET.get('time')

    # Validate date
    try:
        date = timezone.make_aware(datetime.datetime.strptime(date, '%Y-%m-%d'))
    except:
        raise Http404(f'Wrong Date: {date}')
    
    # Validate time
        get_object_or_404(Booking, time=time)

    data = list(Table.objects.all().difference(Table.objects.filter(booking__date=date, booking__time=time)).values())
    
    return JsonResponse(data, safe=False)

@login_required
def book(request):
    
    today = timezone.now()
    admin = request.user.is_superuser or request.user.is_staff

    if request.method == 'GET':

        date = request.GET.get('date', today.day)
        
        # Check if the date in the link is not old or malicious

        try:
            date = timezone.make_aware(datetime.datetime.strptime(date, 'Y-m-d'))
        except:
            date = today
        else:
            date = today if date < today else date

        # prepare a form with date as a starting point
        initial = {'date': date}
        form = AdminBookingForm(initial=initial) if request.user.is_superuser or request.user.is_staff else UserBookingForm(initial=initial)
        min_date = date.strftime('%Y-%m-%d')
        form.fields['date'].widget.attrs.update({'min': min_date})

        if admin:
            bookings = Booking.objects.all()
        else:
            bookings = Booking.objects.filter(
                name=request.user.username,
                date__gte=today)

        data=[]

        for i in bookings:
            list_of_tables=i.get_tables_names()
            time = Booking.BOOKING_TIMES[i.time][1]
            
            data.append({
                'id': i.id,
                'name': i.name,
                'date': i.date,
                'time': time,
                'tables': list_of_tables,
            })

        print(bookings)
        # send the form away!
        return render(
            request, 'bookings/book.html',
            {'form': form, 'bookings': data})

    elif request.method == 'POST':

        if admin:
            form = AdminBookingForm(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = UserBookingForm(request.POST)
            if form.is_valid():
                booking = form.save(commit=False)
                booking.name = request.user.username
                booking.save()
                form.save_m2m()

        return HttpResponseRedirect(reverse('bookings:book_page'))

def edit_booking(request, id):
    return HttpResponse(f'Edit booking {id}')

def delete_booking(request, id):
    return HttpResponse(f'Delete booking {id}')
