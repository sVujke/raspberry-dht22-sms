import Adafruit_DHT as dht 
import api, limit
import time

while(True):
	hum,temp = dht.read_retry(dht.DHT22, 26)

	if temp > limit.temperature or hum >limit.humidity:
		api.sendSms("Temperatura je %d i vlaznost vazduha je %d" %(temp,hum))
		time.sleep(2)