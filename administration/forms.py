from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User, UserManager


class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email',]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is already in use")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class UserAdminCreationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email',]

    def save(self, commit=True):
        user = super(UserAdminCreationForm, self).save(commit=False)
        password = UserManager.generate_password()
        user.set_password(password)
        if commit:
            user.save()
        UserManager.send_activation_link(user.email,password)
        return user


class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (
            'email', 
            'first_name',
            'last_name',
            'password', 
            'active', 
            'admin',
            'principal',
            'student',
            'parent',
            'teacher',
            'student_index',
            'parent1',
            'parent2',
            )

    def clean_password(self):
        return self.initial["password"]
        