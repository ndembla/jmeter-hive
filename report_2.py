import sys, re, math, os
from xml.dom.minidom import parse
from collections import namedtuple

Sample = namedtuple("Sample", ['query', 'duration', 'success', 'end', 'start', 'user']) 

class RawResult(object):
	def __init__(self, fname):
		self.raw = parse(fname)
		self.fname = fname
		samples = self.raw.getElementsByTagName("sample")
		self.samples = list(sorted([self.sample(s) for s in samples], key= lambda v : v.query))
		self.lookup = dict([(s.query, s) for s in self.samples])
		self.queries = set([v.query.split("_")[0] for v in self.samples])
	def sample(self, s):
		attr = lambda a : s.getAttribute(a)
		return Sample(query=attr("lb"), duration=attr("t"), success=attr("s"), end=int(attr("ts")), start=int(attr("ts")) - int(attr("t")), user=attr("tn"))
	def get(self, q, a):
		if (a == 'Run 1'):
			qnamerun = q + '_1'
			if (self.lookup.has_key(qnamerun) and self.lookup[qnamerun].success == 'true'):
				return str(float(self.lookup[qnamerun].duration) / 1000)
			else:
				return "-1"
		elif(a == 'Run 2'):
			qnamerun = q + '_2'
			if (self.lookup.has_key(qnamerun) and self.lookup[qnamerun].success == 'true'):
				return str(float(self.lookup[qnamerun].duration) / 1000)
			else:
				return "-1"
		elif(a == 'Run 3'):
			qnamerun = q + '_3'
			if (self.lookup.has_key(qnamerun) and self.lookup[qnamerun].success == 'true'):
				return str(float(self.lookup[qnamerun].duration) / 1000)
			else:
				return "-1"
		elif(a == 'Run 4'):
			qnamerun = q + '_4'
			if (self.lookup.has_key(qnamerun) and self.lookup[qnamerun].success == 'true'):
				return str(float(self.lookup[qnamerun].duration) / 1000)
			else:
				return "-1"
		else:
			return "-1"

def main(args):
	results = RawResult(args[0]) 
	cols = ["Run 1", "Run 2", "Run 3", "Run 4"] 
        print "Query," + ",".join(cols)
	for r in results.queries:
		if (r.startswith('query')):
			print r + "," + ",".join([results.get(r,c) for c in cols])

if __name__ == "__main__":
	main(sys.argv[1:])
