from django import forms
from django.utils.translation import gettext as _
from front_door.conf import (LOG_ALL, LOG_FAIL, LOG_NONE, LOG_PASS,
                             LOG_RULE_FAIL, LOG_RULE_PASS)


class FrontDoorLogLevel(forms.ChoiceField):
    def __init__(self, **kwargs):
        choices = ([LOG_NONE, _("None")],
                   [LOG_FAIL, "Log Access Deny"],
                   [LOG_PASS, "Log Access Allow"],
                   [LOG_RULE_FAIL, "Log Rule Failure"],
                   [LOG_RULE_PASS, "Log Rule Pass"],
                   [LOG_ALL, "Log Everything"],
                   )
        super().__init__(choices=choices, **kwargs)

    def clean(self, value):
        # value = super().clean(value)
        return int(value)
