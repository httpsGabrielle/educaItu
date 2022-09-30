from django.utils.translation import gettext_lazy as _
from django import forms
from django.db.models import fields
from appMain.models import Games

class Edit_Games(forms.ModelForm):
    class Meta:
        model = Games
        fields = '__all__'
        