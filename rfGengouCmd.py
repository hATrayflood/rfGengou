import datetime
import sys
import optparse
import rfGengou

parser = optparse.OptionParser(usage='Usage: rfGengou [options] [Gengou] Year Month Day')
parser.add_option('--gengou', dest='gengou', help='fix Gengou. (A.D. to Gengou only.)')
parser.add_option('--no-strict', default=False, action='store_true', help='allow out of Gengou range. (Gengou to A.D. only.)')
(options, args) = parser.parse_args()

if len(args) > 3:
	date = rfGengou.g2s(args[0], int(args[1]), int(args[2]), int(args[3]), not options.no_strict)
	if date:
		print(str(date.date()).replace('-', ' '))
else:
	if len(args) == 3:
		date = datetime.datetime(int(args[0]), int(args[1]), int(args[2]))
	else:
		date = datetime.datetime.now()
	wareki = rfGengou.s2g(date, options.gengou)
	if wareki:
		print(u'%s %d %d %d' % wareki)
