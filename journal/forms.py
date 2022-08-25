from django import forms
from journal.models import Journal

import json

def readJson(filename):
    with open(filename, 'r', encoding="utf-8_sig") as fp:
        return json.load(fp)

def get_account():
    # 勘定科目を選択する
    filepath = './static/journal/data/account.json'
    all_data = readJson(filepath)
    accounts = list(all_data.keys())
    all_accounts = [('------'), ('----勘定科目の選択----')]
    for account in accounts:
        all_accounts.append((account, account))
    return all_accounts

class ChoiceAccountForm(forms.Form):
    account = forms.ChoiceField(
        choices = get_account(),
        required = False,
        label = '勘定科目',
        widget = forms.Select(attrs={'class':'form-control', 'id':'id-account'})
    )