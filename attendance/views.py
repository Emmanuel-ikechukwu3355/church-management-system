from django.shortcuts import get_object_or_404, redirect, render

from .models import Attendance
from events.models import Event
from members.models import Member


def attendance_list(request):
    attendances = Attendance.objects.select_related('member', 'event').order_by('-event__date')
    return render(request, 'attendance/attendance_list.html', {
        'attendances': attendances,
    })


def mark_attendance(request):
    events = Event.objects.order_by('-date')
    members = Member.objects.order_by('first_name', 'last_name')

    if request.method == 'POST':
        event_id = request.POST.get('event')
        event = get_object_or_404(Event, id=event_id)

        Attendance.objects.filter(event=event).delete()

        for member in members:
            present_flag = request.POST.get(f'present_{member.id}')
            Attendance.objects.create(
                member=member,
                event=event,
                present=bool(present_flag),
            )

        return redirect('attendance_list')

    return render(request, 'attendance/mark_attendance.html', {
        'events': events,
        'members': members,
    })
