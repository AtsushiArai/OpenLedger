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

## 2022-08-25
試算表を表示するページ trial_balance.html を作成しようとして詰まる。
 * 仕訳テーブルから借方・貸方を集計しようとして、 Journal.objects.all() でデータを取得しようとしたがなぜか仕訳番号しか取得できなかった。仕方なく for ループで Journal.objects.get(pk=pk) として1行ずつ取得した。
 * 取得したデータ(dict形式)をhtmlで表示させようとしたけど表示されなかった。
 * 結局「総勘定元帳テーブル」がないと処理しにくい？「仕訳テーブル」と「総勘定元帳テーブル」は内容がかぶるからどちらか一つにしたい（軽量化のため）。
 * 試算表は view.py の中で完成させたい。どうしたらうまくいくか？

Journalテーブルからviews.pyの trial_balance にデータを引っ張ってきて、 trial_balance の中で仕訳の集計＆期末残高の計算（期首残高どうする？？？）をしたものを trial_balance.html に渡して表示する、みたいなことを実現したい。

## 2022-08-26
昨日の続きで trial_balance.html に取り組んだ。無事に試算表っぽい表示ができるようになった。
月次や四半期ではまだ表示できない。

entry.html で、勘定科目をプルダウンリストで選択できるようにしようとして詰まる。
プルダウンリストは作れたが、その値をどのようにPUSHすれば仕訳テーブルに取り込めるかわからなかった。