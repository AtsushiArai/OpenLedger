from dal import autocomplete

from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.utils.timezone import localtime

from journal.forms import ChoiceAccountForm
from journal.models import Journal, Account, BeginningBalance

# Create your views here.
def test(request):
    context = {}
    form = ChoiceAccountForm()
    context['accounts'] = form
    return render(request, "journal/test2.html", context)

def index(request):
    return render(request, "journal/index.html")

def debit_side(request):
    return render(request, "journal/debit_side.html")

def credit_side(request):
    return render(request, "journal/credit_side.html")


def entry(request, *args, **kwargs):
    context = {}
    form = ChoiceAccountForm(initial={
        "debit_account": 11101
    })
    context['accounts'] = form

    if request.method == "GET":
        return render(request, "journal/entry.html", context)
    
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
        posted_debit_account = request.POST.getlist('account')[0::2]                # プルダウンリストで選択された値が "account" として借方・貸方とも渡される。リストにまとめられたうち、indexの偶数番目が借方、奇数番目が貸方になる。 
        posted_debit_sub_account = request.POST.getlist('debit-sub-account')
        posted_debit_consumptiontax = request.POST.getlist('debit-consumptiontax')
        posted_debit_department = request.POST.getlist('debit-department')
        posted_debit_amount = request.POST.getlist('debit-amount')
        posted_debit_company = request.POST.getlist('debit-company')
        posted_debit_side = request.POST.getlist('debit-credit')[0::2]


        # 貸方
        posted_credit_account = request.POST.getlist('account')[1::2]
        posted_credit_sub_account = request.POST.getlist('credit-sub-account')
        posted_credit_consumptiontax = request.POST.getlist('credit-consumptiontax')
        posted_credit_department = request.POST.getlist('credit-department')
        posted_credit_amount = request.POST.getlist('credit-amount')
        posted_credit_company = request.POST.getlist('credit-company')
        posted_credit_side = request.POST.getlist('debit-credit')[1::2]

        # その他
        posted_descreption = request.POST.getlist('description')

        sum_posted_debit_amount = 0
        sum_posted_credit_amount = 0

        for x in posted_debit_amount:
            sum_posted_debit_amount += int(x)

        for y in posted_credit_amount:
            sum_posted_credit_amount += int(y)

        if sum_posted_debit_amount != sum_posted_credit_amount:
            error_message = "借方・貸方の金額合計が一致しません。"
            context['error_message'] = error_message
            context['value'] = {
                "je_number":posted_je_number,
                "je_row_number": posted_je_row_number,
                "annual": posted_annual,
                "accounting_date": posted_accounting_date,
                "entry_type": posted_entry_type,
                "debit_account1": posted_debit_account[0],
                "debit_sub_account1": posted_debit_sub_account[0],
                "debit_consumptiontax1": posted_debit_consumptiontax[0],
                "debit_department1": posted_debit_department[0],
                "debit_amount1": posted_debit_amount[0],
                "debit_company1": posted_debit_company[0],
                "debit_account2": posted_debit_account[1],
                "debit_sub_account2": posted_debit_sub_account[1],
                "debit_consumptiontax2": posted_debit_consumptiontax[1],
                "debit_department2": posted_debit_department[1],
                "debit_amount2": posted_debit_amount[1],
                "debit_company2": posted_debit_company[1],
                "credit_account1": posted_credit_account[0],
                "credit_sub_account1": posted_credit_sub_account[0],
                "credit_consumptiontax1": posted_credit_consumptiontax[0],
                "credit_department1": posted_credit_department[0],
                "credit_amount1": posted_credit_amount[0],
                "credit_company1": posted_credit_company[0],
                "credit_account2": posted_credit_account[1],
                "credit_sub_account2": posted_credit_sub_account[1],
                "credit_consumptiontax2": posted_credit_consumptiontax[1],
                "credit_department2": posted_credit_department[1],
                "credit_amount2": posted_credit_amount[1],
                "credit_company2": posted_credit_company[1],
                "description1": posted_descreption[0],
                "description2": posted_descreption[1],
            }
            return render(request, "journal/entry.html", context)

        else:

            for a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p in zip(
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
                posted_debit_side,              #o
                posted_credit_side              #p
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
                        je_debit_credit = p,
                    )

                    journal_entry_credit.save()

        return render(request, "journal/entry.html", context)

def make_trial_balance(request):
    # 仕訳テーブルから勘定科目ごとの借方・貸方発生額の集計を行う。

    # {勘定科目コード: 勘定科目名} dict 作成
    account_dict = dict()
    i = Account.objects.all().count()

    for pk in range(1, i+1):
        try:
            acc = Account.objects.get(pk=pk)
            code = acc.account_code
            name = acc.account_name
            account_dict[code] = name
        except:
            pass


    # [科目コード, 科目名, 期首残高, 借方発生額, 貸方発生額 , 期末残高] list 作成
    ## 開始残高の取得
    beginning_balance_dict = dict()
    i = BeginningBalance.objects.all().count()

    for pk in range(1, i+1):
        try:
            bb = BeginningBalance.objects.get(pk=pk)
            ac = bb.account_code
            am = bb.beginning_balance
            beginning_balance_dict[ac] = am
        except:
            pass

    # 借方・貸方発生額の取得と集計
    trial_balance = dict()
    i = Journal.objects.all().count()

    for pk in range(1, i+1):
        try:
            je = Journal.objects.get(pk=pk)
            dc = je.je_debit_credit
            ac = je.je_account
            ac_name = account_dict[ac]
            am = je.je_amount

            ## 抽出した仕訳の勘定科目が、まだ trial_balance に出てきていない場合
            if ac not in trial_balance:
                if dc == "0":
                    trial_balance[ac] = [am, 0]
                else:
                    trial_balance[ac] = [0, am]

            ## 抽出した仕訳の勘定科目が、 trial_balance にある場合
            else:
                if dc == "0":
                    dev_am = trial_balance[ac][0] + am
                    cre_am = trial_balance[ac][1]
                    trial_balance[ac] = [dev_am, cre_am]
                else:
                    cre_am = trial_balance[ac][1] + am
                    dev_am = trial_balance[ac][0]
                    trial_balance[ac] = [dev_am, cre_am]
        except:
            pass
    
    # 勘定科目コード順に sort
    sorted_trial_balance = sorted(trial_balance.items(), key=lambda x:x[0])

    # sorted_trial_balance を for ループしつつ、以下を行う：
        # 科目名の追加
        # 期首残高の追加
        # 期末残高の追加
    fixed_trial_balance = []

    for code, dc in sorted_trial_balance:
        bb = beginning_balance_dict[code]
        if code[0] == ("1" or "5" or "6" or "9") or code[0:1] == ("72" or "82"):
            fixed_trial_balance.append([code, account_dict[code], bb, dc[0], dc[1], bb + dc[0] - dc[1]])

        else:
            fixed_trial_balance.append([code, account_dict[code], bb, dc[0], dc[1], bb - dc[0] + dc[1]])

    # accounts_list = [x for x in Account.objects.all()]
    # print(accounts_list)

    # all_accounts = Account.objects.all()
    # accounts_list = []
    # i = 0
    # for ac in all_accounts:
    #     accounts_list.append(ac)
    #     i += 1
    #     if i == 5:
    #         break
    # print(accounts_list)


    # accounts_table = [x for x in Account.objects.values()]
    # accounts_list = []
    # for d in accounts_table:
    #     accounts_list.append(d["account_code"]+" "+d["account_name"])

    # for a in accounts_list:
    #     print(a)
    #     break

    # htmlに "trial_balance" として渡す。
    return render(request, "journal/trial_balance.html", context={"trial_balance":fixed_trial_balance})

class AccountsAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        qs = Account.objects.all()
        if self.q:
            qs = qs.filter()

        return qs