from django import forms
from .models import Feedback
from django.utils.translation import gettext

class MessageForm(forms.Form):
    message = forms.CharField(
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': gettext('Введите сообщение...')}),
        label=''
    )

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['feedback']
        widgets = {
            "feedback": forms.Textarea(attrs={'id':'feed-back', 'placeholder': "Оставить отзыв или вопрос"})
        }
    