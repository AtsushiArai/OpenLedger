from django.contrib import admin

from journal.models import Journal, Account, SubAccount, Companies, Users, Department, Annual
# Register your models here.

admin.site.register(Journal)
admin.site.register(Account)
admin.site.register(SubAccount)
admin.site.register(Companies)
admin.site.register(Users)
admin.site.register(Department)
admin.site.register(Annual)