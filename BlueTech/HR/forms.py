from django.forms import ModelForm

from HR.models import EmailFiles, Salary


class EmailsForm(ModelForm):
    class Meta:
        model = EmailFiles
        fields = '__all__'


class PayrollForm(ModelForm):
    class Meta:
        model = Salary
        fields = '__all__'
