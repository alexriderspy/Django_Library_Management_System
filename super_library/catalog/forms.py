import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class GrantRequestForm(forms.Form):
    name=forms.CharField(max_length=100)
    bookinstpk=forms.CharField(max_length=200)
            