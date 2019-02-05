import shodan
import sys

SHODAN_API_KEY = "SHODAN_API_KEY"

api = shodan.Shodan(SHODAN_API_KEY)
PAGE = sys.argv[1]
PAGE2 = int(PAGE) + 1
try:
        # Search Shodan
        results = api.search('http.title:"Node-RED"', page=PAGE)

        # Show the results
        print 'Results found: %s' % results['total']
       
        for result in results['matches']:
		try:
			if result['ssl']:
                		print "https://" + result['ip_str'].rstrip() + ":" + str(result['port'])
			
		except:
			print "http://" + result['ip_str'].rstrip() + ":" + str(result['port'])
except shodan.APIError, e:
        print 'Error: %s' % e

try:
        # Search Shodan
        results = api.search('http.title:"Node-RED"', page=PAGE2)

      
       
                
        for result in results['matches']:
		try:
			if result['ssl']:
                		print "https://" + result['ip_str'].rstrip() + ":" + str(result['port'])
			
		except:
			print "http://" + result['ip_str'].rstrip() + ":" + str(result['port'])
except shodan.APIError, e:
        print 'Error: %s' % e
