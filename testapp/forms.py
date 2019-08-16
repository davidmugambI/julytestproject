from django import forms
from testapp.models import testdata


class SendDataForm(forms.Form):
    studentName = forms.CharField(max_length=30)
    course = forms.CharField(max_length=20)
    age = forms.IntegerField()
    email = forms.EmailField()


class sendDataModelForm(forms.ModelForm):
    # edit fields here

    class Meta:
        model = testdata
        # fields = ('studentName', 'course', 'age', 'email')
        # exclude =('age',)
        fields = '__all__'

class UpdateForm(forms.ModelForm):
    # edit fields here

    class Meta:
        model = testdata
        # fields = ('studentName', 'course', 'age', 'email')
        # exclude =('age',)
        fields = '__all__'
