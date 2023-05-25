from django import forms

class ScoreForm(forms.Form):
    atlet_score_kiri = forms.IntegerField(widget=forms.NumberInput())
    atlet_score_kanan = forms.IntegerField(widget=forms.NumberInput())
