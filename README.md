rfGengou
========
http://rayflood.org/diary-temp/rfGengou-0.3.zip  
rfGengou.py 明治から平成までの元号と西暦を変換するライブラリです。
* 日単位で判定、年単位で変換できます。
* 通常は元号の有効範囲内で計算するため、元号の年月日のチェックにも使えます。
* 追加引数を指定することで、元号の有効範囲を超えた仮想年数も計算できます。
* 元号の定義については、以下のサイトを参考にしました。  
http://www.kumamotokokufu-h.ed.jp/kumamoto/bungaku/wa_seireki.html

使い方
------
    >>> import rfGengou
    >>> (gengou, year, month, day) = rfGengou.s2g(datetime.datetime(2011, 6, 9))
    >>> datetime = rfGengou.g2s(rfGengou.HEISEI.gengou, 23, 6, 9)
    >>> print datetime
    2011-06-09 00:00:00

注意！
------
平成の最終日は2087/12/31(平成99年)と仮定しています。根拠はなし。  
明治より前の元号、平成の次の元号は対応していません。  
明治の最終日と大正の初日、大正の最終日と昭和の初日が重複しています。  
ここでは次の元号の初日を優先してます。  
あくまで判定が日単位なだけです。旧暦などの日数シフトは対応していません。  
pythonのdatetimeの制約により、西暦換算で1年から9999年まで計算可能です。  

コマンドラインツール
--------------------
rfgengou コマンドが使えます。
日付を引数に指定すると変換処理を行います。

github
------
https://github.com/hATrayflood/rfGengou

launchpad
---------
https://launchpad.net/~h-rayflood/+archive/python2

License
-------
The MIT License (MIT)  
http://opensource.org/licenses/mit-license.php  
