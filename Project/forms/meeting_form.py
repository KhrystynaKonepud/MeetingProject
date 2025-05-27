from django import forms
from Project.models.meeting import Meeting
from Project.models.user import User

class MeetingForm(forms.ModelForm):
    participants = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Запросити учасників"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.start_time:
            self.initial['start_time'] = self.instance.start_time.strftime('%Y-%m-%dT%H:%M')

    class Meta:
        model = Meeting
        fields = ['title', 'start_time', 'duration', 'room_name', 'participants']
        widgets = {
            'start_time': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'form-control',
                },
                format='%Y-%m-%dT%H:%M'
            ),
        }

    def save(self, commit=True):
        meeting = super().save(commit)
        if commit and self.cleaned_data.get('participants'):
            from Project.models.participant import Participant
            Participant.objects.filter(meeting=meeting).delete()
            for user in self.cleaned_data['participants']:
                Participant.objects.create(meeting=meeting, user=user)
        return meeting
