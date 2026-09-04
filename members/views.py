from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import Member
from .forms import MemberForm


def member_list(request):

    query = request.GET.get('q')

    members = Member.objects.all().order_by('-date_joined')

    if query:
        members = members.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query)
        )

    return render(
        request,
        'members/member_list.html',
        {
            'members': members,
            'query': query,
        }
    )


def add_member(request):

    if request.method == 'POST':

        form = MemberForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('member_list')

    else:
        form = MemberForm()

    return render(
        request,
        'members/member_form.html',
        {
            'form': form,
            'title': 'Add Member',
        }
    )


def edit_member(request, member_id):

    member = get_object_or_404(Member, id=member_id)

    if request.method == 'POST':

        form = MemberForm(
            request.POST,
            instance=member
        )

        if form.is_valid():
            form.save()
            return redirect('member_list')

    else:
        form = MemberForm(instance=member)

    return render(
        request,
        'members/member_form.html',
        {
            'form': form,
            'title': 'Edit Member',
        }
    )


def delete_member(request, member_id):

    member = get_object_or_404(
        Member,
        id=member_id
    )

    if request.method == 'POST':

        member.delete()

        return redirect('member_list')

    return render(
        request,
        'members/member_confirm_delete.html',
        {
            'member': member,
        }
    )