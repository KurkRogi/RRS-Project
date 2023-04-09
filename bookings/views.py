from django.shortcuts import (
    render, redirect, get_object_or_404, get_list_or_404)
from django.http import (
    HttpResponse, HttpResponseRedirect, Http404, JsonResponse)
from django.utils import timezone
import datetime
from bookings.forms import UserBookingForm, AdminBookingForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Table, Booking


def index(request):
    return render(request, 'bookings/index.html')


def check_available_tables(request):
    date = request.GET.get('date')
    time = request.GET.get('time')

    # Check if date is real
    try:
        date = timezone.make_aware(
            datetime.datetime.strptime(date, '%Y-%m-%d'))
    except ValueError:
        print('DATE')
        return JsonResponse([{}], safe=False)

    # Check if time is real
    try:
        next((t for t in Booking.BOOKING_TIMES if t[0] == int(time)))
    except (StopIteration, TypeError, ValueError) as error:
        print('TIME ', time)
        print('ERROR ', error)
        print('REQUEST', request)
        return JsonResponse([{}], safe=False)

    data = list(Table.objects.all().difference(
        Table.objects.filter(booking__date=date, booking__time=time))
        .values())

    return JsonResponse(data, safe=False)


@login_required
def book(request):

    today = timezone.now()
    admin = request.user.is_superuser or request.user.is_staff

    if request.method == 'GET':

        date = request.GET.get('date', today.strftime('Y-m-d'))

        # Check if the date in the link is not old or malicious
        try:
            date = timezone.make_aware(
                datetime.datetime.strptime(date, '%Y-%m-%d'))
        except ValueError:
            date = today
        
        # prepare a form with date as a starting point
        initial = {'date': date}
        form = (
            AdminBookingForm(initial=initial) if admin
            else UserBookingForm(initial=initial))
        min_date = today.strftime('%Y-%m-%d')
        form.fields['date'].widget.attrs.update({'min': min_date})

        if admin:
            bookings = Booking.objects.all() 
        else:
            bookings = Booking.objects.filter(
                name=request.user.username,
                date__gte=today)

        old_bookings = bookings.filter(date__lt=today).exists()
        data = []

        for b in bookings:

            # list_of_tables = b.get_tables_names()
            # seraching in list of tuples with
            # generator expression technique from:
            # https://stackoverflow.com/questions/2917372/how-to-search-a-list-of-tuples-in-python
            # time = Booking.BOOKING_TIMES[next((
            #     i for i, v in enumerate(Booking.BOOKING_TIMES)
            #     if v[0] == b.time), 0)][1]

            data.append({
                'id': b.id,
                'name': b.name,
                'date': b.date,
                'time': b.get_time_display(),
                'tables': b.get_tables_names(),
            })

        # send the form away!
        return render(
            request, 'bookings/book.html',
            {'form': form, 'bookings': data, 'old_bookings': old_bookings})

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

        return redirect('bookings:book_page')

@login_required
def edit_booking(request, id):
    booking = get_object_or_404(Booking, pk=id)
    admin = request.user.is_superuser or request.user.is_staff

    if not (admin or request.user.username == booking.name):
        raise Http404("No such a booking available")

    if request.method == 'GET':
        form = (
            AdminBookingForm(instance=booking) if admin
            else UserBookingForm(instance=booking))

        return render(request, 'bookings/edit.html', {'form': form, 'id': id})
    elif request.method == "POST":
        if admin:
            form = AdminBookingForm(request.POST)
            if form.is_valid():
                booking = form.save(commit=False)
                booking.id = id
                booking.save()
                form.save_m2m()
        else:
            form = UserBookingForm(request.POST)
            if form.is_valid():
                booking = form.save(commit=False)
                booking.id = id
                booking.name = request.user.username
                booking.save()
                form.save_m2m()
        return redirect('bookings:book_page')
    else:
        raise Http404("Service not available")

@login_required
def delete_booking(request, id):
    get_object_or_404(Booking, id=id).delete()

    return redirect('bookings:book_page')


def delete_past_bookings(request):
    if request.user.is_superuser:
        Booking.objects.filter(date__lt=timezone.now()).delete()
    
    return redirect('bookings:book_page')
