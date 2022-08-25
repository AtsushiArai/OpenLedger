from django.conf import settings
from django.db import models

# Create your models here.

# 仕訳テーブル
class Journal(models.Model):
    # 仕訳番号（主キー）
    je_number = models.CharField('仕訳番号', max_length=8)
    # 仕訳行番号
    je_row_number = models.CharField('仕訳行番号', max_length=5)
    # 年度（コード番号を保持）
    je_annual = models.CharField('年度コード', max_length=5)
    # 計上年月日
    je_accounting_date = models.DateTimeField('計上年月日',)
    # 入力年月日（自動入力）
    je_entry_date = models.DateTimeField('入力年月日', auto_now_add=True)
    # 計上区分（コード番号を保持）
    je_entry_type = models.CharField('計上区分', max_length=1)
    # 貸借区分（コード番号を保持）
    je_debit_credit = models.CharField('貸借区分', max_length=1)
    # 勘定科目（コード番号を保持）
    je_account = models.CharField('勘定科目コード', max_length=5)
    # 補助科目（コード番号を保持）
    je_subaccount = models.CharField('補助科目コード', max_length=5)
    # 消費税区分（コード番号を保持）
    je_consumptiontax = models.CharField('消費税区分', max_length=2)
    # 計上部門（コード番号を保持）
    je_department = models.CharField('計上部門コード', max_length=5)
    # 金額
    je_amount = models.IntegerField('金額', )
    # 取引先名（コード番号を保持）
    je_company = models.CharField('取引先コード', max_length=5)
    # 摘要
    je_description = models.CharField('摘要', max_length=100)

    def __str__(self):
        return self.je_number



# 勘定科目テーブル
class Account(models.Model):
    # 勘定科目CD（5ケタ）
    account_code = models.CharField('勘定科目コード', max_length=5)
        # 資産：10000 -> 流動資産 11000, 固定資産 12000, 繰延資産 13000
        # 負債：20000 -> 流動負債 21000, 固定負債 22000
        # 純資産：30000 -> 株主資本 31000, 評価・換算差額 31000
        # 売上高：40000 -> 売上高 41000
        # 売上原価：50000 -> 商品売上原価 51000, 製造原価 52000
        # 販管費：60000
        # 営業外損益：70000 -> 営業外収益 71000, 営業外費用 72000
        # 特別損益：80000 -> 特別利益 81000, 特別損失 82000
        # 税金等：90000 -> 法人税等 91000, 法人税等調整額 92000, 非支配株主持分損益 93000
    # 勘定科目名
    account_name = models.CharField('勘定科目名', max_length=20)

    def __str__(self):
        return self.account_code + " " + self.account_name


# 補助科目テーブル
class SubAccount(models.Model):
    # 補助科目CD（5ケタ）
    subaccount_code = models.CharField('補助科目コード', max_length=5)
    # 補助科目名
    subaccount_name = models.CharField('補助科目名', max_length=20)

    def __str__(self):
        return self.subaccount_code + " " + self.subaccount_name


# 総勘定元帳テーブル
class GeneralLedger():
    pass


# 試算表テーブル
class TrialBalance(Account):
    def __init__():
        pass

    def make_trial_balance():
        # 期首残高
        beginning_balance = models.IntegerField("期首残高")
        # 借方金額
        debit_amount = models.IntegerField("借方金額")
        # 貸方金額
        credit_amount = models.IntegerField("貸方金額")
        # 期末残高
        ending_balance = models.IntegerField("期末残高")
    

# 得意先テーブル
class Companies(models.Model):
    # 得意先コード
    campany_code = models.CharField('得意先コード', max_length=5)
    # 得意先名
    campany_name = models.CharField('得意先名', max_length=50)

    def __str__(self):
        return self.campany_code + " " + self.campany_name



# ユーザーテーブル
class Users(models.Model):
    # ユーザーコード
    user_code = models.CharField('ユーザーコード', max_length=5)
    # ユーザー名
    user_name = models.CharField('ユーザー名', max_length=20)
    # 権限コード
    user_authority_code = models.CharField('権限コード', max_length=1)
    # 権限名
    user_authority_name = models.CharField('権限名', max_length=5)

    def __str__(self):
        return self.user_code + " " + self.user_name



# 部門テーブル
class Department(models.Model):
    # 部門コード
    department_code = models.CharField('部門コード', max_length=5)
    # 部門名
    department_name = models.CharField('部門名', max_length=20)

    def __str__(self):
        return self.department_code + " " + self.department_name



# 年度テーブル
class Annual(models.Model):
    # 年度コード
    annual_code = models.CharField('年度コード', max_length=2)
    # 年度名
    annual_name = models.CharField('年度名', max_length=10)

    def __str__(self):
        return self.annual_code + " " + self.annual_name



# 貸借区分テーブル
class DebitCredit(models.Model):
    # 貸借コード -> 0:借方, 1:貸方
    debit_credit_code = models.CharField('貸借区分コード', max_length=1)
    # 貸借名
    debit_credit_name = models.CharField('貸借区分名', max_length=2)

    def __str__(self):
        return self.debit_credit_code + " " + self.debit_credit_name



# 消費税区分テーブル
class ConsumptionTax(models.Model):
    # 消費税区分コード
    consumption_tax_code = models.CharField('消費税区分コード', max_length=2)
    # 消費税区分名
    consumption_tax_name = models.CharField('消費税区分名', max_length=10)

    def __str__(self):
        return self.consumption_tax_code + " " + self.consumption_tax_name



# 計上区分テーブル（日常、月次決算、四半期決算、年次決算）
class JournalType(models.Model):
    # 計上区分コード -> 1:日常, 2:月次, 3:四半期, 4:年次
    journal_type_code = models.CharField('計上区分コード', max_length=1)
    # 計上区分名
    journal_type_name = models.CharField('計上区分名', max_length=3)

    def __str__(self):
        return self.journal_type_code + " " + self.journal_type_name

