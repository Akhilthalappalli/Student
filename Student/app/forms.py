from django import forms
from app.models import Student,Admin


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if (len(str(phone)) != 10):
            raise forms.ValidationError('Invalid Phone number , Phone number must be 10 digits')
        return phone


    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        SpecialSym =['$', '@', '#', '%']


        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(("The two password fields didn't match."))

            elif len(password2) < 8:
                raise forms.ValidationError(("Make sure your password is at lest 8 letters"))
            elif not any(char.isdigit() for char in password2):
                raise forms.ValidationError(("Make sure your password has a number in it"))
            elif not any(char.isupper() for char in password2):
                raise forms.ValidationError(("Make sure your password has a capital letter in it"))
            elif not any(char in SpecialSym for char in password2):
                raise forms.ValidationError(("Make sure your password has a symbols  in it"))

            return password2

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        SpecialSym =['$', '@', '#', '%']


        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(("The two password fields didn't match."))

            elif len(password2) < 8:
                raise forms.ValidationError(("Make sure your password is at lest 8 letters"))
            elif not any(char.isdigit() for char in password2):
                raise forms.ValidationError(("Make sure your password has a number in it"))
            elif not any(char.isupper() for char in password2):
                raise forms.ValidationError(("Make sure your password has a capital letter in it"))
            elif not any(char in SpecialSym for char in password2):
                raise forms.ValidationError(("Make sure your password has a symbols  in it"))

            return password2
