from django.forms import ModelForm
from TestTask1.main.models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person