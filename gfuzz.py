 #!/bin/env python3.7

from banner import Banner
import requests, optparse, webbrowser, re
Banner()
parse = optparse.OptionParser()
parse.add_option('-w','--wordlist', help='Comand for wordlist', dest='wd', metavar='filename')
parse.add_option('-c','--code', help='Code to search', dest='cd', metavar='200', type=int)
parse.add_option('-s','--site', help='Website to search', dest='st', metavar='https://targeturl.com/')
parse.add_option('-n','--no', help='does not show 404 URLs',action='store_false', dest='ur')
parse.add_option('-o','--open', help='Open in browser found URLs',action='store_true', dest='op')
regex = re.compile(r'^(http|https):[\/]{2}(www\.)?[\w]+([\-\.]{1}[\w]+)*\.[a-z]{2,5}[\/]{1}')



(options, args) = parse.parse_args()
arq = open(options.wd, 'r')
rg = regex.search(options.st)
if rg is not None:
	url = rg.group()
	for i in arq:
		i = i.strip()
		completeUrl = url+i
		r = requests.get(completeUrl)
		check = r.status_code
		if check == options.cd:
			print(f'[ + ]FOUND {completeUrl} | CODE {check}')
			if options.op:
				webbrowser.open(completeUrl)
		elif options.ur == False:
			print(f'[ - ]NOT FOUND {completeUrl} | CODE {check}')
else:
	print(f'Erro: {options.st} não se satisfaz como URL')
			
arq.close()