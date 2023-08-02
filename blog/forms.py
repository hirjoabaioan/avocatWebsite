from django import forms
from .models import Întrebări, Contact


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Întrebări
        fields = ('title', 'email', 'body')


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs\
            .update({
            'id': 'name',
            'class': 'model-form'
        })
        self.fields['email'].widget.attrs\
            .update({
            'id': 'emaila',
            'class': 'model-form'
        })
        self.fields['subject'].widget.attrs\
            .update({
            'id': 'subject',
            'class': 'model-form'
        })
        self.fields['message'].widget.attrs\
            .update({
            'id': 'message',
            'class': 'model-form'
        })    