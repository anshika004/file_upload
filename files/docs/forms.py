from django import forms

class UploadFileForm(forms.Form):
    file=forms.FileField(widget=forms.ClearableFileInput(attrs={'allow_multiple_selected':True}))