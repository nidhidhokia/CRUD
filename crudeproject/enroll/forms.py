from django import forms
from enroll.models import User 

class StudentRegistration(forms.ModelForm):
 class Meta:
  model = User
  fields = ['roll_no','name','email','division','address']
  widgets = {
      'roll_no': forms.TextInput(attrs={'class':'form-control'}),
      'name': forms.TextInput(attrs={'class':'form-control'}),
      'email': forms.EmailInput(attrs={'class':'form-control'}),
      'division': forms.TextInput(attrs={'class':'form-control'}),
      'address': forms.TextInput(attrs={'class':'form-control'}),
  }