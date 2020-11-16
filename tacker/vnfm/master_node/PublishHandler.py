import redis
import json
def publisher(instance_id,cause,name,type):
    r = redis.Redis(host='192.168.1.103', port=6379, db=0)
    payload = {}
    payload['instance_id'] = instance_id
    payload['cause'] = cause
    payload['name'] = name
    payload['type'] = type
    payload_values = json.dumps(payload)
    print('Send vnf instance fault report')
    r.publish(
        'error_report',
        payload_values
    )
