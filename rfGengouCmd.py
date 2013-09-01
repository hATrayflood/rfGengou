import datetime
import sys
import optparse
import rfGengou

GENGOU_LIST = [rfGengou.HEISEI, rfGengou.SHOUWA, rfGengou.TAISHOU, rfGengou.MEIJI]
gengou_map = {}
for g in GENGOU_LIST:
	gengou_map[g.gengou] = g

parser = optparse.OptionParser(usage='Usage: rfGengou [options] [Gengou] Year Month Day')
parser.add_option('--gengou', dest='gengou', help='fix Gengou. (A.D. to Gengou only.)')
parser.add_option('--no-strict', default=False, action='store_true', help='allow out of Gengou range. (Gengou to A.D. only.)')
(options, args) = parser.parse_args()

if len(args) > 3:
	gengou = gengou_map[unicode(args[0], sys.stdin.encoding)].gengou
	date = rfGengou.g2s(gengou, int(args[1]), int(args[2]), int(args[3]), not options.no_strict)
	if date:
		print(str(date.date()).replace('-', ' '))
	else:
		print
else:
	if len(args) == 3:
		date = datetime.datetime(int(args[0]), int(args[1]), int(args[2]))
	else:
		date = datetime.datetime.now()
	if options.gengou:
		gengou = gengou_map[unicode(options.gengou, sys.stdin.encoding)]
	else:
		gengou = None
	date = rfGengou.s2g(date, gengou)
	if date:
		print(u'%s %d %d %d' % date)
	else:
		print
