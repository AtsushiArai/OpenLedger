from django.urls import path

from journal import views


urlpatterns = [
    path("", views.entry, name="entry"),
    path("debit_side", views.debit_side, name="debit_side"),
    path("credit_side", views.credit_side, name="credit_side"),
    path("trial_balance", views.make_trial_balance, name="trial_balance"),
    path("balance_sheet", views.make_balance_sheet, name="balance_sheet"),
    path("profit_loss_statement", views.make_profit_loss_statement, name="profit_loss_statement"),
    path("test", views.test, name="test"),
]