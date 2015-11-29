import urllib2
import time
from sinchsms import SinchSMS

expected_price=4000

print "start"
url='http://www.flipkart.com/seagate-backup-plus-slim-1-tb-external-hard-drive/p/itmdswy5zzg9myjv?pid=ACCDSWY49TJFFXHG&ref=L%3A6231378520028825767&srno=p_4'
response=urllib2.urlopen(url).read()
line=response.find('selling-price omniture-field')
response=response[line:]
pos_rs=response.find('Rs')
pos_span=response.find('</span>')

print response[pos_rs+4:pos_span]

price=0

def sms(msg):
	number='+919421701789'
	key='d7428c4f-6ac0-4b16-9e7c-299f079b3334'
	secret='sVLKck4OJkaFKK8KbCrxgw=='
	client=SinchSMS(key,secret)

	print "here"
	
	print msg
	
	response=client.send_message(number,msg)
	message_id=response['MessageId']
	response=client.check_status(message_id)
	
	while response['Status']!='Successful':
		print "Wait..!!"
		time.sleep(1)

	print "!!..Message Send Successfully..!!"



for v in response[pos_rs+4:pos_span]:
	if v!=',':
		price=price*10 + int(v)

print price
if price - expected_price <= 760:
	msg='price is in expected range and current price is'+str(price)
	sms(sms)
