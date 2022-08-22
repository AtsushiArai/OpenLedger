from socket import fromshare
from django import forms
from journal.models import Journal

class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = (
            'je_number',
            'je_row_number',
            'je_annual',
            'je_accounting_date',
            'je_entry_date',
            'je_entry_type',
            'je_account',
            'je_subaccount',
            'je_consumptiontax',
            'je_department',
            'je_amount',
            'je_description'
        )