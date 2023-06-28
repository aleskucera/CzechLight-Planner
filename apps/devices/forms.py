# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import LineDegreeModel, AddDropModel, ClientModel


# class LineDegreeForm(forms.ModelForm):
#     class Meta:
#         model = LineDegreeModel
#         fields = ['name', 'description', 'latitude', 'longitude', 'ip_address']
#         labels = {
#             'name': 'Device Name',
#             'description': 'Description',
#             'latitude': 'Latitude',
#             'longitude': 'Longitude',
#             'ip_address': 'IP Address',
#         }

class LineDegreeForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Device Name',
                'class': 'form-control'
            }
        )
    )

    ip_address = forms.CharField(
        label='IP Address',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Device IP Address',
                'class': 'form-control'
            }
        )
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Device Description',
                'class': 'form-control',
                'rows': '3'
            }
        )
    )

    latitude = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'latitude',
                'placeholder': 'Device Latitude',
                'class': 'form-control'
            }
        )
    )

    longitude = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'longitude',
                'placeholder': 'Device Longitude',
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = LineDegreeModel
        fields = ('name', 'ip_address', 'description', 'latitude', 'longitude')


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
