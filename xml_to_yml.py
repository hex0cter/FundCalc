import xmltodict, json

import glob, os

missing = open('/tmp/missing', 'w', 0)

for in_file in glob.glob("data/hist/*.txt"):
	out_file = in_file.replace('.txt', '.yml')

	if os.path.isfile(out_file):
		# print "%s skipped because %s already exists" % (in_file, out_file)
		continue

	f = open(in_file, 'r')
	c = f.read()
	f.close()

	try:
		o = xmltodict.parse(c)
	except:
		print "Unable to parse %s" % in_file
		missing.write(os.path.basename(in_file).split('.')[0] + '\n')
		continue

	j = json.dumps(o, sort_keys=True, indent=4, separators=(',', ': '))
	f = open(out_file, 'w')
	f.write(j)
	f.close

	print "successfully parsed %s" % in_file

missing.close
