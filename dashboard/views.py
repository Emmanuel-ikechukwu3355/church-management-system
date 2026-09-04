from django.shortcuts import render
from django.utils import timezone

from members.models import Member
from events.models import Event
from attendance.models import Attendance


def dashboard(request):
    today = timezone.localdate()

    total_members = Member.objects.count()

    total_events = Event.objects.count()

    attendance_today = Attendance.objects.filter(
        event__date=today,
        present=True
    ).count()

    first_day_of_month = today.replace(day=1)

    new_members_this_month = Member.objects.filter(
        date_joined__gte=first_day_of_month
    ).count()

    context = {
        'total_members': total_members,
        'total_events': total_events,
        'attendance_today': attendance_today,
        'new_members_this_month': new_members_this_month,
    }

    return render(request, 'dashboard.html', context)