from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Table(models.Model):

    name = models.CharField(max_length=10)
    description = models.CharField(max_length=100, blank=True)
    sits = models.IntegerField(default=4)

    def __str__(self):
        return f'Table {self.name} ({self.sits})'


class Booking(models.Model):

    BOOKING_TIMES = (
        (0, "16:00"),
        (2, "17:00"),
        (4, "18:00"),
        (6, "19:00"),
        (8, "20:00"),
        (10, "21:00"),
        (12, "22:00"),
    )

    name = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    time = models.IntegerField(default=1)
    tables = models.ManyToManyField(Table, blank=True)

    def __str__(self):
        return f'{self.name} booked for {self.date.strftime("%-d %B %Y")}'

    def get_tables_names(self):
        q = self.tables.all()
        l = len(q)
        r = ""
        for i in range(l):
            r += f"{q[i].name} ({q[i].sits})"
            r += " | " if i < l-1 else ""
        return r


    class Meta:
        ordering = ['date', 'time']
