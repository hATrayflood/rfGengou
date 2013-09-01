# -*- coding: utf-8 -*-

# rfGengou.py 明治から平成までの元号と西暦を変換するライブラリです。
# ・日単位で判定、年単位で変換できます。
# ・通常は元号の有効範囲内で計算するため、元号の年月日のチェックにも使えます。
# ・追加引数を指定することで、元号の有効範囲を超えた仮想年数も計算できます。
# ・元号の定義については、以下のサイトを参考にしました。
#   http://www.kumamotokokufu-h.ed.jp/kumamoto/bungaku/wa_seireki.html
#
# 使い方：
u"""
>>> import rfGengou
>>> (gengou, year, month, day) = rfGengou.s2g(datetime.datetime(2011, 6, 9))
>>> datetime = rfGengou.g2s(rfGengou.HEISEI.gengou, 23, 6, 9)
>>> print datetime
2011-06-09 00:00:00
"""
#
# 注意！：
#  平成の最終日は2087/12/31(平成99年)と仮定しています。根拠はなし。
#  明治より前の元号、平成の次の元号は対応していません。
#  明治の最終日と大正の初日、大正の最終日と昭和の初日が重複しています。
#  ここでは次の元号の初日を優先してます。
#  あくまで判定が日単位なだけです。旧暦などの日数シフトは対応していません。
#  pythonのdatetimeの制約により、西暦換算で1年から9999年まで計算可能です。

import datetime

class rfGengou:
	def __init__(self):
		self.GENGOU_LIST = [HEISEI, SHOUWA, TAISHOU, MEIJI]
		#self.GENGOU_LIST = [MEIJI, TAISHOU, SHOUWA, HEISEI]

	def s2g(self, date, gengou = None):
		u"""
		>>> rfgg = rfGengou()
		>>> print rfgg.s2g(datetime.date(1868,  9,  7))
		None
		>>> print u"%s %2d年 %2d月 %2d日" % rfgg.s2g(datetime.date(1868,  9,  8))
		明治  1年  9月  8日
		>>> print u"%s %2d年 %2d月 %2d日" % rfgg.s2g(datetime.date(1912,  7, 30))
		大正  1年  7月 30日
		>>> print u"%s %2d年 %2d月 %2d日" % rfgg.s2g(datetime.date(1926, 12, 25))
		昭和  1年 12月 25日
		>>> print u"%s %2d年 %2d月 %2d日" % rfgg.s2g(datetime.date(1989,  1,  7))
		昭和 64年  1月  7日
		>>> print u"%s %2d年 %2d月 %2d日" % rfgg.s2g(datetime.date(1989,  1,  8))
		平成  1年  1月  8日
		>>> print u"%s %2d年 %2d月 %2d日" % rfgg.s2g(datetime.date(2087, 12, 31))
		平成 99年 12月 31日
		>>> print rfgg.s2g(datetime.date(2088,  1,  1))
		None

		>>> print u"%s %2d年 %2d月 %2d日" % rfgg.s2g(datetime.date(1868,  9,  7), HEISEI)
		平成 -120年  9月  7日
		>>> print u"%s %2d年 %2d月 %2d日" % rfgg.s2g(datetime.date(2868,  9,  7), HEISEI)
		平成 880年  9月  7日
		>>> print u"%s %2d年 %2d月 %2d日" % rfgg.s2g(datetime.date(1950,  1,  1), TAISHOU)
		大正 39年  1月  1日
		>>> print u"%s %2d年 %2d月 %2d日" % rfgg.s2g(datetime.date(1950,  1,  1), HEISEI)
		平成 -38年  1月  1日
		>>> taika = rfGengouRange(u"大化"  , datetime.datetime( 645,  6, 19), datetime.datetime( 650,  2, 15))
		>>> rfgg.GENGOU_LIST.append(taika)
		>>> print u"%s %2d年 %2d月 %2d日" % rfgg.s2g(datetime.date(646,  1,  1))
		大化  2年  1月  1日
		"""
		d = datetime.date(date.year, date.month, date.day)
		if gengou:
			return gengou.adjustS(d)
		for n in self.GENGOU_LIST:
			if n.inboundS(d):
				return n.adjustS(d)

	def g2s(self, gengou, year, month, day, strict = True):
		u"""
		>>> rfgg = rfGengou()
		>>> print rfgg.g2s(MEIJI.gengou  ,  1,  9,  7)
		None
		>>> print rfgg.g2s(MEIJI.gengou  ,  1,  9,  8)
		1868-09-08 00:00:00
		>>> print rfgg.g2s(MEIJI.gengou  , 45,  7, 30)
		1912-07-30 00:00:00
		>>> print rfgg.g2s(MEIJI.gengou  , 45,  7, 31)
		None
		>>> print rfgg.g2s(TAISHOU.gengou,  1,  7, 29)
		None
		>>> print rfgg.g2s(TAISHOU.gengou,  1,  7, 30)
		1912-07-30 00:00:00
		>>> print rfgg.g2s(TAISHOU.gengou, 15, 12, 25)
		1926-12-25 00:00:00
		>>> print rfgg.g2s(TAISHOU.gengou, 15, 12, 26)
		None
		>>> print rfgg.g2s(SHOUWA.gengou ,  1, 12, 24)
		None
		>>> print rfgg.g2s(SHOUWA.gengou ,  1, 12, 25)
		1926-12-25 00:00:00
		>>> print rfgg.g2s(SHOUWA.gengou , 64,  1,  7)
		1989-01-07 00:00:00
		>>> print rfgg.g2s(SHOUWA.gengou , 64,  1,  8)
		None
		>>> print rfgg.g2s(HEISEI.gengou ,  1,  1,  7)
		None
		>>> print rfgg.g2s(HEISEI.gengou ,  1,  1,  8)
		1989-01-08 00:00:00
		>>> print rfgg.g2s(HEISEI.gengou , 99, 12, 31)
		2087-12-31 00:00:00
		>>> print rfgg.g2s(HEISEI.gengou ,100,  1,  1)
		None

		>>> print rfgg.g2s(HEISEI.gengou, -63,  1,  1, False)
		1925-01-01 00:00:00
		>>> print rfgg.g2s(HEISEI.gengou, 163,  1,  1, False)
		2151-01-01 00:00:00
		>>> uchuu = rfGengouRange(u"宇宙暦", datetime.datetime(2087,  3,  7), datetime.datetime(9999, 12, 31))
		>>> rfgg.GENGOU_LIST.append(uchuu)
		>>> print rfgg.g2s(uchuu.gengou, 772,  1,  1)
		2858-01-01 00:00:00
		"""
		for n in self.GENGOU_LIST:
			if n.inboundG(gengou, year, month, day) or not strict:
				return n.adjustG(year, month, day)

class rfGengouRange:
	def __init__(self, gengou, start, end):
		self.gengou = gengou
		self.start  = start
		self.end    = end
		self.diffyear  = start.year - 1

	def inboundS(self, date):
		d = datetime.datetime(date.year, date.month, date.day)
		if d < self.start:
			return False
		if d > self.end:
			return False
		return True

	def inboundG(self, gengou, year, month, day):
		if not self.gengou == gengou:
			return False
		return self.inboundS(self.adjustG(year, month, day))

	def adjustS(self, date):
		return (self.gengou, date.year - self.diffyear, date.month, date.day)

	def adjustG(self, year, month, day):
		return datetime.datetime(year + self.diffyear, month, day)

HEISEI  = rfGengouRange(u"平成", datetime.datetime(1989,  1,  8), datetime.datetime(2087, 12, 31))
SHOUWA  = rfGengouRange(u"昭和", datetime.datetime(1926, 12, 25), datetime.datetime(1989,  1,  7))
TAISHOU = rfGengouRange(u"大正", datetime.datetime(1912,  7, 30), datetime.datetime(1926, 12, 25))
MEIJI   = rfGengouRange(u"明治", datetime.datetime(1868,  9,  8), datetime.datetime(1912,  7, 30))

def s2g(date, gengou = None):
	return rfGengou().s2g(date, gengou)

def g2s(gengou, year, month, day, strict = True):
	return rfGengou().g2s(gengou, year, month, day, strict)

if __name__ == "__main__":
	import doctest
	doctest.testmod()
