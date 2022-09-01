from django.contrib import admin

from journal.forms import ChoiceAccountForm, ChoiceAccountForm2
from journal.models import Journal, Account, SubAccount, Companies, Users, Department, Annual, BeginningBalance, TestTable
# Register your models here.

admin.site.register(Journal)
admin.site.register(SubAccount)
admin.site.register(Companies)
admin.site.register(Users)
admin.site.register(Department)
admin.site.register(Annual)

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    model = Account
    list_display = ('account_code', 'account_name')
    list_editable = ('account_name',)

@admin.register(BeginningBalance)
class BeginningBalanceAdmin(admin.ModelAdmin):
    model = BeginningBalance
    list_display = ('account_code', 'beginning_balance')
    list_editable = ('beginning_balance',)


@admin.register(TestTable)
class TestAdmin(admin.ModelAdmin):
    form = ChoiceAccountForm2