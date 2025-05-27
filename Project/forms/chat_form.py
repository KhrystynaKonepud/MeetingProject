from django import forms
from Project.models.chatRoom import ChatRoom
from Project.models.message import Message


class ChatRoomForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ['name', 'participants']  # ← поле is_private видалено
        widgets = {
            'participants': forms.CheckboxSelectMultiple
        }


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text', 'file']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].required = False
        self.fields['file'].required = False  # якщо теж не хочеш обов’язковим

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get('text')
        file = cleaned_data.get('file')

        if not text and not file:
            raise forms.ValidationError("Введіть текст або прикріпіть файл.")

        return cleaned_data
