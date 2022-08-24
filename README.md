# OpenLedger



# 作業記録

## 2022-08-22　〜 2022-08-23
topページ、仕訳入力ページを作成。
models.pyにデータベースのテーブルを構築。

entryページで、仕訳の貸借が横に並ぶように表示させようと思い <iframe> と debit_side.html（子）, credit_side.html（子） を使って表示させるところまではできたが、
いざentry.html（親）でsubmitしてみたら子要素の情報がPOSTできなかった。解決できず保留中。

## 2022-08-24
勘定科目リストを作成。
地道にadmin画面に打ち込んだのち、 manage.py dumpdata journal.account > account.json にて出力。
vscodeのjson整形機能に思わず「おー」と声が出た。
Gitを入れていたものの add, commit, push していなかったので、これらを実行

* Gitカンペ
  * git add .
  * git commit
  * git push origin main
