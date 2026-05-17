from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm


def event_list(request):
    events = Event.objects.order_by('-date')
    return render(request, 'events/event_list.html', {'events': events})


def add_event(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('event_list')
    return render(request, 'events/event_form.html', {'form': form, 'title': 'Add Event'})


def edit_event(request, id):
    event = get_object_or_404(Event, id=id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('event_list')
    return render(request, 'events/event_form.html', {'form': form, 'title': 'Edit Event'})


def delete_event(request, id):
    event = get_object_or_404(Event, id=id)
    event.delete()
    return redirect('event_list')
