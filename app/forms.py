from django import forms
from app.models import *
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets={'password':forms.PasswordInput}
        help_texts={'username':''}
