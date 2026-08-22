from django import forms
from .models import member

class MemeberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'phone', 'email', 'address', 'gender']

