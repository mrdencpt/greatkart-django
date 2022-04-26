from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'ระบุรหัสผ่าน'
    }))
    
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'ยืนยันรหัสผ่าน'
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'ระบุชื่อ'
        self.fields['last_name'].widget.attrs['placeholder'] = 'นามสกุล'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'เบอร์โทร'
        self.fields['email'].widget.attrs['placeholder'] = 'อีเมล์'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "รหัสผ่าน 2 ช่องไม่ตรงกัน! กรุณาแก้ไข"
            )