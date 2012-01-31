from django import forms
from django.conf import settings

class JQueryDateWidget(forms.DateInput):
    class Media:
        js = (
            settings.STATIC_URL + "js/jquery-ui.js",
            settings.STATIC_URL + "js/datewidget.js",)
        css = {
            'all': (settings.STATIC_URL + 'css/smoothness/jquery-ui-1.8.17.custom.css',)
        }

    def __init__(self, attrs={}, format=None):
        super(JQueryDateWidget, self).__init__(attrs={'id': 'jqDateField', 'size': '10'}, format=format)
