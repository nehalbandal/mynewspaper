from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'username', 'fullname', 'dob', 'gender', 'bio', 'profile_pic')

        widgets = {
            'dob': DateInput(),
            'bio': forms.Textarea(attrs={"rows": 3, "cols": 40, "placeholder": "Say something about yourself..."})
        }


class CustomUserChangeForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'fullname', 'dob', 'gender', 'bio', 'profile_pic')

        widgets = {
            'dob': DateInput(),
            'bio': forms.Textarea(attrs={"rows": 3, "cols": 40, "placeholder": "Say something about yourself..."})
        }