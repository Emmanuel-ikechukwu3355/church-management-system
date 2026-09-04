from django import forms
from .models import Member


class MemberForm(forms.ModelForm):

    class Meta:
        model = Member

        fields = [
            'first_name',
            'last_name',
            'phone',
            'email',
            'address',
            'gender',
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter first name'
            }),

            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter last name'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address'
            }),

            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter address',
                'rows': 3
            }),

            'gender': forms.Select(attrs={
                'class': 'form-select'
            }),
        }