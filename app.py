import json
import datetime

order = {
	"orderID":12345,
	"shopper_name":"Ivan Ivanov",
	"shopper_email":"ivanov@example.com",
	"contents":[
		{
			"product_id":34,
			"product_name":"Super product",
			"quantity":1
		},
		{
			"product_id":56,
			"product_name":"Wonderful product",
			"quantity":3
		}
	],
	"order_completed":True
}

#from dict to json
order_json = json.dumps(order)
#from json to dict
order2 = json.loads(order_json)
print('Shopper name: ',order2['shopper_name'])

true = json.dumps(True) #return 'true'

#there's an exception when trying to convert some objects

now = datetime.datetime.utcnow()
try:
    now_json = json.dumps(now)
except TypeError as err:
    print('As I promised there\'s an exception:', err)
#it happens because json can not define time and date types
#we can turn 'now' into something json understands, like string or epoch
now_str = str(now)
now_json = json.dumps(now_str) #it works
print('json understands strings: ', now_json)

#to make epoch we need to import 'mktime' from 'time' module

from time import mktime

now_epoch = int(mktime(now.timetuple()))
now_epoch_json = json.dumps(now_epoch) #it works as well
print('json understands epoch as well:', now_epoch_json)

#instead of repeating these steps again and again we can change the way json will be encoded

class DTEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return int(mktime(obj.timetuple()))
        return json.JSONEncoder.default(self, obj)

try:
    now_json2 = json.dumps(now, cls=DTEncoder)
except Exception as err:
    print('sorry...', err)
else:
    now_epoch2 = json.loads(now_json2)
    print('one more epoch',now_epoch2)
