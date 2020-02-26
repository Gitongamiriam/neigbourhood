from django import forms
from .models import Profile,Neighbourhood,Posts,Business

class NewMessageForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ['name', 'pub_date']