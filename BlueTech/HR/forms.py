from django.forms import ModelForm

from HR.models import EmailFiles


class EmailsForm(ModelForm):
    class Meta:
        model = EmailFiles
        fields = '__all__'
