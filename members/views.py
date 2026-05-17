# from django.shortcuts import render
# from .models import Member

# def member_list(request):
#     members = Member.objects.all()
#     return render(request, 'members/member_list.html', {'members': members})


from django.shortcuts import get_object_or_404, redirect, render

from .forms import MemberForm
from .models import Member


def add_member(request):
    form = MemberForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('member_list')
    return render(request, 'members/member_form.html', {'form': form})


def edit_member(request, id):
    member = get_object_or_404(Member, id=id)
    form = MemberForm(request.POST or None, instance=member)
    if form.is_valid():
        form.save()
        return redirect('member_list')
    return render(request, 'members/member_form.html', {'form': form})


def delete_member(request, id):
    member = get_object_or_404(Member, id=id)
    member.delete()
    return redirect('member_list')

from datetime import date

from django.db.models import Count, Q
from django.db.models.functions import TruncMonth


def member_list(request):
    query = request.GET.get('q')
    if query:
        members = Member.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query)
        )
    else:
        members = Member.objects.all()

    return render(request, 'members/member_list.html', {
        'members': members,
        'query': query,
    })


def dashboard(request):
    today = date.today()
    total_members = Member.objects.count()
    members_this_month = Member.objects.filter(
        date_joined__year=today.year,
        date_joined__month=today.month,
    ).count()

    monthly_growth = (
        Member.objects
        .annotate(month=TruncMonth('date_joined'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )

    gender_data = (
        Member.objects
        .values('gender')
        .annotate(count=Count('id'))
        .order_by('gender')
    )

    male_count = Member.objects.filter(gender='Male').count()
    female_count = Member.objects.filter(gender='Female').count()

    from attendance.models import Attendance
    from events.models import Event

    attendance_count = Attendance.objects.count()
    total_events = Event.objects.count()

    return render(request, 'members/dashboard.html', {
        'total_members': total_members,
        'members_this_month': members_this_month,
        'monthly_growth': monthly_growth,
        'gender_data': gender_data,
        'male_count': male_count,
        'female_count': female_count,
        'attendance_count': attendance_count,
        'total_events': total_events,
    })