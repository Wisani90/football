from django import forms
 
class PostForm(forms.Form):
    league_id = forms.CharField(max_length=16)