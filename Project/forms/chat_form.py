from django import forms
from Project.models.chatRoom import ChatRoom
from Project.models.message import Message

class ChatRoomForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ['name', 'is_private', 'participants']
        widgets = {
            'participants': forms.CheckboxSelectMultiple
        }

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text', 'file']
