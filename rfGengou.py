# -*- coding: utf-8 -*-

# rfGengou.py 明治から平成までの元号と西暦を変換するライブラリです。
# ・日単位で判定、年単位で変換できます。
# ・通常は元号の有効範囲内で計算するため、元号の年月日のチェックにも使えます。
# ・追加引数を指定することで、元号の有効範囲を超えた仮想年数も計算できます。
# ・元号の定義については、以下のサイトを参考にしました。
#   http://www.kumamotokokufu-h.ed.jp/kumamoto/bungaku/wa_seireki.html
#
# 使い方：
#  import rfGengou
#  (gengou, year, month, day) = rfGengou.s2g(datetime.datetime(2011, 6, 9))
#  datetime = print rfGengou.g2s(rfGengou.HEISEI.gengou, 23, 6, 9)
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

HEISEI  = rfGengou(u"平成", datetime.datetime(1989,  1,  8), datetime.datetime(2087, 12, 31))
SHOUWA  = rfGengou(u"昭和", datetime.datetime(1926, 12, 25), datetime.datetime(1989,  1,  7))
TAISHOU = rfGengou(u"大正", datetime.datetime(1912,  7, 30), datetime.datetime(1926, 12, 25))
MEIJI   = rfGengou(u"明治", datetime.datetime(1868,  9,  8), datetime.datetime(1912,  7, 30))
GENGOU_LIST = [HEISEI, SHOUWA, TAISHOU, MEIJI]
#GENGOU_LIST = [MEIJI, TAISHOU, SHOUWA, HEISEI]

def s2g(date, gengou = None):
	d = datetime.date(date.year, date.month, date.day)
	for n in GENGOU_LIST:
		if n.inboundS(d) or n.gengou == gengou:
			return n.adjustS(d)

def g2s(gengou, year, month, day, strict = True):
	for n in GENGOU_LIST:
		if n.inboundG(gengou, year, month, day) or not strict:
			return n.adjustG(year, month, day)

# テスト
if __name__ == "__main__":
	def p_s2g(date, gengou = None):
		s = str(date) + " : "
		o = s2g(date, gengou)
		if o:
			s += u"%s %2d年 %2d月 %2d日" % o
		else:
			s += str(o)
		print(s)

	def p_g2s(gengou, year, month, day, strict = True):
		s  = u"%s %2d年 %2d月 %2d日 " % (gengou, year, month, day)
		s += " : " + str(g2s(gengou, year, month, day, strict))
		print(s)

	"""
	1868-09-07 : None
	1868-09-08 : 明治  1年  9月  8日
	1912-07-30 : 大正  1年  7月 30日
	1926-12-25 : 昭和  1年 12月 25日
	1989-01-07 : 昭和 64年  1月  7日
	1989-01-08 : 平成  1年  1月  8日
	2087-12-31 : 平成 99年 12月 31日
	2088-01-01 : None
	"""
	p_s2g(datetime.date(1868,  9,  7))
	p_s2g(datetime.date(1868,  9,  8))
	p_s2g(datetime.date(1912,  7, 30))
	p_s2g(datetime.date(1926, 12, 25))
	p_s2g(datetime.date(1989,  1,  7))
	p_s2g(datetime.date(1989,  1,  8))
	p_s2g(datetime.date(2087, 12, 31))
	p_s2g(datetime.date(2088,  1,  1))

	print
	"""
	明治  1年  9月  7日  : None
	明治  1年  9月  8日  : 1868-09-08 00:00:00
	明治 45年  7月 30日  : 1912-07-30 00:00:00
	明治 45年  7月 31日  : None
	大正  1年  7月 29日  : None
	大正  1年  7月 30日  : 1912-07-30 00:00:00
	大正 15年 12月 25日  : 1926-12-25 00:00:00
	大正 15年 12月 26日  : None
	昭和  1年 12月 24日  : None
	昭和  1年 12月 25日  : 1926-12-25 00:00:00
	昭和 64年  1月  7日  : 1989-01-07 00:00:00
	昭和 64年  1月  8日  : None
	平成  1年  1月  7日  : None
	平成  1年  1月  8日  : 1989-01-08 00:00:00
	平成 99年 12月 31日  : 2087-12-31 00:00:00
	平成 100年  1月  1日  : None
	"""
	p_g2s(MEIJI.gengou  ,  1,  9,  7)
	p_g2s(MEIJI.gengou  ,  1,  9,  8)
	p_g2s(MEIJI.gengou  , 45,  7, 30)
	p_g2s(MEIJI.gengou  , 45,  7, 31)
	p_g2s(TAISHOU.gengou,  1,  7, 29)
	p_g2s(TAISHOU.gengou,  1,  7, 30)
	p_g2s(TAISHOU.gengou, 15, 12, 25)
	p_g2s(TAISHOU.gengou, 15, 12, 26)
	p_g2s(SHOUWA.gengou ,  1, 12, 24)
	p_g2s(SHOUWA.gengou ,  1, 12, 25)
	p_g2s(SHOUWA.gengou , 64,  1,  7)
	p_g2s(SHOUWA.gengou , 64,  1,  8)
	p_g2s(HEISEI.gengou ,  1,  1,  7)
	p_g2s(HEISEI.gengou ,  1,  1,  8)
	p_g2s(HEISEI.gengou , 99, 12, 31)
	p_g2s(HEISEI.gengou , 100,  1,  1)

	print
	"""
	1868-09-07 : 平成 -120年  9月  7日
	2868-09-07 : 平成 880年  9月  7日
	平成 -63年  1月  1日  : 1925-01-01 00:00:00
	平成 163年  1月  1日  : 2151-01-01 00:00:00
	"""
	p_s2g(datetime.date(1868,  9,  7), HEISEI.gengou)
	p_s2g(datetime.date(2868,  9,  7), HEISEI.gengou)
	p_g2s(HEISEI.gengou, -63,  1,  1, False)
	p_g2s(HEISEI.gengou, 163,  1,  1, False)

	print
	"""
	0646-01-01 : 大化  2年  1月  1日
	宇宙暦 772年  1月  1日  : 2858-01-01 00:00:00
	"""
	taika = rfGengou(u"大化"  , datetime.datetime( 645,  6, 19), datetime.datetime( 650,  2, 15))
	uchuu = rfGengou(u"宇宙暦", datetime.datetime(2087,  3,  7), datetime.datetime(9999, 12, 31))
	GENGOU_LIST.append(taika)
	GENGOU_LIST.append(uchuu)
	p_s2g(datetime.date(646,  1,  1))
	p_g2s(uchuu.gengou, 772,  1,  1)
