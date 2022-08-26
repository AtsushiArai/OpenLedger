from django import forms
from journal.models import Account

accounts_table = [x for x in Account.objects.values()]
accounts_list = []
for d in accounts_table:
    accounts_list.append((d["account_code"],d["account_code"]+" "+d["account_name"]))


""" 
MEMO1:accounts_table の中身
    accounts_table = [
        {"id":1, "account_code": "11102", "account_name":"小口現金"},
        {"id":2, "account_code": "11110", "account_name":"当座預金"},
        ......
    ]

MEMO2:
ChoiceField の choices に渡す値は、(some1, some2) となっていないとダメっぽい。

error -> accounts_list = [code+name, code+name, .....]

success -> accounts_list = [(code, code+name), (code, code+name),....]


"""
class ChoiceAccountForm(forms.Form):
    account = forms.fields.ChoiceField(
        choices=accounts_list,
        required=True,
    )

class JournalEntryForm(forms.Form):
    je_number = forms.CharField(required=True)
    je_row_number = forms.CharField(required=True)
    je_annual = forms.CharField(required=True)
    je_accountint_date = forms.DateField(required=True)
    je_entry_date = forms.DateField(required=True)
    je_entry_type = forms.CharField(required=True)
    je_debit_credit = forms.CharField(required=True)
    je_account = ChoiceAccountForm()
    je_consumptiontax = forms.CharField()
    je_department = forms.CharField()
    je_amount = forms.CharField()
    je_company = forms.CharField()
    je_description = forms.CharField()
    