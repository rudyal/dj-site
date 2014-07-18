from django import forms
from django.forms import ModelForm, Textarea
from polls.models import Choice, Poll, PictureObject
# What to import ??

class PictureObjectForm(ModelForm):
	class Meta:
		model = PictureObject
		fields = ('title', 'source', 'text', 'tags1', 'gender', 'date', 'picture', 'tags')
		widgets = {
			'text': Textarea(attrs={'cols': 80, 'rows': 2}),
		}
        # title = forms.CharField(max_length=200, required=True)
        # source = forms.CharField(max_length=400, required=False)
        # text = forms.CharField(max_length=10000, required=False)
        # tags = forms.CharField(max_length=10000, required=False)
        # gender = forms.CharField(max_length=10, required=False)
        # date = forms.CharField(max_length=60, required=False)
        # picture = forms.CharField(max_length=60, required=False)
