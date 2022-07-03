from django import forms

from .models import SentEmail, Communication

class EmailForm(forms.ModelForm):

    class Meta:
        model = SentEmail
        fields = ['subject','content']

class CommunicationForm(forms.ModelForm):

    class Meta:
        model = Communication
        fields = ['customer','comm_detail','timestamp']
