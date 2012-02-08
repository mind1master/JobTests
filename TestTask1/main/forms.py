from TestTask1.main.widgets import JQueryDateWidget
from django.forms import ModelForm
from TestTask1.main.models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.fields['birth_date'].widget = JQueryDateWidget()
