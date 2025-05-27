from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from Project.forms.meeting_form import MeetingForm
from Project.models.meeting import Meeting


@login_required
def meetings_view(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            meeting = form.save(commit=False)
            meeting.owner = request.user
            meeting.save()
            form.save()
            return redirect('meeting')
    else:
        form = MeetingForm()

    meetings = Meeting.objects.filter(owner=request.user)

    return render(request, 'meeting.html', {
        'form': form,
        'meetings': meetings,
    })


@login_required
def edit_meeting(request, meeting_id):
    meeting = get_object_or_404(Meeting, pk=meeting_id, owner=request.user)
    if request.method == 'POST':
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return redirect('meeting')
    else:
        form = MeetingForm(instance=meeting)

    return render(request, 'edit_meeting.html', {
        'form': form,
        'meetings': meeting,
    })

@login_required
def invitations_view(request):
    # Отримати всі зустрічі, на які користувача запросили
    invited_meetings = Meeting.objects.filter(participant__user=request.user)
    return render(request, 'invitations.html', {
        'invited_meetings': invited_meetings
    })
