#!/usr/bin/env python3

import sys
import re

def trans(match=str):
	match=match.split('.')
	s=str()
	for i in match:
		s+='{:0^8b}'.format(int(i))
	return s.count('1')

if __name__=='__main__':
	reg=re.compile(r'\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}\b')
	if len(sys.argv) > 1:
		for i in sys.argv:
			if reg.match(i):
				print(i, '==>', trans(i))
	try:
		while 1:
			i=input()
			if reg.match(i):
				print(i, '==>', trans(i))
	except:
		sys.exit(0)
