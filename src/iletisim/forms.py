from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','phone', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'İsim'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Telefon'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail'}),
            # 'subject': forms.ChoiceField(attrs={'placeholder': 'Talebiniz'}),
            'message': forms.Textarea(attrs={'placeholder': 'Mesaj'}),
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'medium-input bg-white margin-25px-bottom'


