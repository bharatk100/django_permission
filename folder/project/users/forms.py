from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .models import Profile, CHOICE_GENDER


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    CHOICE_GENDER = ((1, 'Male'), (2, 'Female'))
    gender = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={"required": "required"}),
                               choices=CHOICE_GENDER)

    class Meta:
        model = User
        fields = ('username', 'email', 'gender', 'password1', 'password2',)

    def save(self, commit=True):
        user = super().save(commit=False)

        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.gender = self.cleaned_data['gender']

        if commit:
            user.save()
        return user


"""
for "Creating___________Custom Fields__________ with registration form "
"""


class ProfileFrom(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('gender', 'image')


"""
___________________________________________________for________Updating Profile FORM______________
"""


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileUpdateForm(forms.ModelForm):
    CHOICE_GENDER = ((1, 'Male'), (2, 'Female'))
    gender = forms.ChoiceField(required=True, widget=forms.RadioSelect(), choices=CHOICE_GENDER)

    class Meta:
        model = Profile
        fields = ['gender', 'image']

