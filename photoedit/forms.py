from django import forms
 
# crop image
class CropImageForm(forms.Form):
    name = forms.CharField(max_length=255)
    image = forms.ImageField()

    def __str__(self):
        return f"{self.name}"
