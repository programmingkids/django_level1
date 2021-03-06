from django import forms


class Work01Form (forms.Form):
    name = forms.CharField(
        label = "名前",
        initial = "",
        widget=forms.TextInput(attrs={"class" : "form-control"}))
    mail = forms.EmailField(
        label = "メール",
        initial = "",
        widget=forms.EmailInput(attrs={"class" : "form-control"}))
    age = forms.IntegerField(
        label = "年齢",
        initial = "",
        widget=forms.NumberInput(attrs={"class" : "form-control"}))

