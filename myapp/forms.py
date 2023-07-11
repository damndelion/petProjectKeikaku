from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import ReviewAnime


# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, label='Search')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewAnime
        fields = ['rating', 'content']



