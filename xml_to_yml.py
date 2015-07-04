import xmltodict, json

import glob



for in_file in glob.glob("data/hist/*.txt"):
	out_file = in_file.replace('.txt', '.yml')

	f = open(in_file, 'r')
	c = f.read()
	f.close()
	o = xmltodict.parse(c)
	j = json.dumps(o, sort_keys=True, indent=4, separators=(',', ': '))
	print j
	f = open(out_file, 'w')
	f.write(j)
	f.close
	print in_file, out_file