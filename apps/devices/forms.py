# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from .models import DeviceModel
from apps.device_config import device_types


class DeviceForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Device Name',
                'class': 'form-control'
            }
        )
    )
    # Create choices for the device type field. Also add the placeholder.
    device_type = forms.ChoiceField(
        label='Device Type',
        choices=[('placeholder', 'Select Device Type')] + device_types,
        widget=forms.Select(
            attrs={
                'id': 'device-type',
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
        required=False,
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
        model = DeviceModel
        fields = ('name', 'ip_address', 'description', 'latitude', 'longitude')
