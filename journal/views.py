from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.utils.timezone import localtime

from journal.models import Journal, Account

# Create your views here.
def test(request):
    return render(request, "journal/test.html")

def index(request):
    return render(request, "journal/index.html")

def debit_side(request):
    return render(request, "journal/debit_side.html")

def credit_side(request):
    return render(request, "journal/credit_side.html")

def entry(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, "journal/entry.html")
    
    # request.method == "POST"
    else:

        # 借方・貸方　共通
        posted_je_number = str(request.POST["je-number"])
        posted_je_row_number = request.POST.getlist("je-row-number")
        posted_annual = str(request.POST['annual'])
        posted_accounting_date = str(request.POST['accounting-date'])
        posted_entry_date = localtime(timezone.now())
        posted_entry_type = str(request.POST.get('entry-type'))

        # 借方
        posted_debit_account = request.POST.getlist('debit-account')
        posted_debit_sub_account = request.POST.getlist('debit-sub-account')
        posted_debit_consumptiontax = request.POST.getlist('debit-consumptiontax')
        posted_debit_department = request.POST.getlist('debit-department')
        posted_debit_amount = request.POST.getlist('debit-amount')
        posted_debit_company = request.POST.getlist('debit-company')
        posted_debit_credit = request.POST.getlist('debit-credit')

        # 貸方
        posted_credit_account = request.POST.getlist('credit-account')
        posted_credit_sub_account = request.POST.getlist('credit-sub-account')
        posted_credit_consumptiontax = request.POST.getlist('credit-consumptiontax')
        posted_credit_department = request.POST.getlist('credit-department')
        posted_credit_amount = request.POST.getlist('credit-amount')
        posted_credit_company = request.POST.getlist('credit-company')
        posted_debit_credit = request.POST.getlist('debit-credit')

        # その他
        posted_descreption = request.POST.getlist('description')

        print("JE Number", posted_je_number)
        print("Debit Account", posted_debit_account)
        print("Credit Account", posted_credit_account)

        for a,b,c,d,e,f,g,h,i,j,k,l,m,n,o in zip(
            posted_je_row_number,           #a
            posted_debit_account,           #b
            posted_debit_sub_account,       #c
            posted_debit_consumptiontax,    #d
            posted_debit_department,        #e
            posted_debit_amount,            #f
            posted_debit_company,           #g
            posted_credit_account,          #h
            posted_credit_sub_account,      #i
            posted_credit_consumptiontax,   #j
            posted_credit_department,       #k
            posted_credit_amount,           #l
            posted_credit_company,          #m
            posted_descreption,             #n
            posted_debit_credit             #o
            ):

            if b != "":
                journal_entry_debit = Journal(
                    je_number=posted_je_number,
                    je_row_number = a,
                    je_annual = posted_annual,
                    je_accounting_date = posted_accounting_date,
                    je_entry_date = posted_entry_date,
                    je_entry_type = posted_entry_type,
                    je_account = b,
                    je_subaccount = c,
                    je_consumptiontax = d,
                    je_department = e,
                    je_amount = int(f),
                    je_company = g,
                    je_description = n,
                    je_debit_credit = o,
                )
                journal_entry_debit.save()
            
            if h != "":
                journal_entry_credit = Journal(
                    je_number=posted_je_number,
                    je_row_number = a,
                    je_annual = posted_annual,
                    je_accounting_date = str(posted_accounting_date),
                    je_entry_date = str(posted_entry_date),
                    je_entry_type = posted_entry_type,
                    je_account = h,
                    je_subaccount = i,
                    je_consumptiontax = j,
                    je_department = k,
                    je_amount = int(l),
                    je_company = m,
                    je_description = n,
                    je_debit_credit = o,
                )

                journal_entry_credit.save()

        return render(request, "journal/entry.html")

def trial_balance(request):
    # 仕訳テーブルから勘定科目ごとの借方・貸方発生額の集計を行う。
    tb = dict()
    i = Journal.objects.all().count()
    for pk in range(1, i+1):
        je = Journal.objects.get(pk=pk)
        dc = je.je_debit_credit
        ac = je.je_account
        am = je.je_amount

        if ac not in tb:
            if dc == "0":
                tb[ac] = [am, 0]
            else:
                tb[ac] = [0, am]
        else:
            if dc == "0":
                dev_am += tb[ac][0]
                cre_am = tb[ac][1]
                tb[ac] = [dev_am, cre_am]
            else:
                cre_am += tb[ac][1]
                dev_am = tb[ac][0]
                tb[ac] = [dev_am, cre_am]
    
    # sorted_tb = sorted(tb.items(), key=lambda x:x[0])
    # print(sorted_tb)
    # print(sorted_tb[0])
    # print(sorted_tb[0][0])
    # print(sorted_tb[0][1])
    # print(sorted_tb[0][1][0])

    # 集計結果を出力する。
    print(tb)
    
    return render(request, "journal/trial_balance.html", tb)
