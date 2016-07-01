import urllib
import urllib2
import util

params = {}

params['api_key'] = util.api_key
params['api_secret'] = util.api_secert
params['to'] = util.to_number
params['from'] = util.from_number
#params['text'] = util.msg_text


def sendSms(text):
	params['text'] = text
	url = 'https://rest.nexmo.com/sms/json?' + urllib.urlencode(params)

	request = urllib2.Request(url)
	print 'request sent'
	request.add_header('Accept', 'application/json')
	response = urllib2.urlopen(request)
