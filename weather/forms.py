from django import forms
from crispy_forms.helper import FormHelper


class CityForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper._help_text_inline = None
        self.helper.label_class = None
        self.helper.form_show_labels = False
        self.helper.form_show_errors = False
        self.helper.error_text_inline = None
        self.helper.form_error_title = None
        self.helper.form_error_title = None

    city = forms.CharField(
        required=True,
        label=None,
        max_length=100,
        error_messages={
            "required": "This field can't be null."
        },
        
    )
    city.help_text = None
    city.widget.attrs.update(
        {
            'autocomplete': 'street-address',
            'autofocus': True,
        }
    )