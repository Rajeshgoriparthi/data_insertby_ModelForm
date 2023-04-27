from django import forms
from app.models import *


class Topic_Forms(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'


class Player_Forms(forms.ModelForm):
    class Meta:
        model=Player
        fields='__all__'
        