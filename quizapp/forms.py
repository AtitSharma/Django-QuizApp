from django import forms
from . models import Answer
from django.contrib.auth.forms import UserCreationForm
from quizapp.models import User
class AnswerCheckForm(forms.ModelForm):
    class Meta:
        model=Answer
        fields=["question","answer"]

class UserRegistaionForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","password1","password2"]

        