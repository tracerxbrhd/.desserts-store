from django import forms
from .models import ChatMessage


class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = (
            'content',
        )
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full'
            })
        }