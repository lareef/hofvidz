from .models import Video
from django import forms

class Videoform(forms.ModelForm):
    class Meta:
        model = Video
        # fields = ['title', 'url', 'youtube_id']
        # labels = {'youtube_id':'YouTube Id'}
        fields = ['url']
        labels = {'url':'YouTube Url'}

class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=255, label='Search for video ')