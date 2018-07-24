from django import forms

class CommentForm(forms.Form):
    text = forms.CharField(label='Your Comment', max_length=100)
    meal_id = forms.IntegerField()
    user_id = forms.IntegerField()