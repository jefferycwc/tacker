from flask import Flask,render_template,request,jsonify
import requests
#import os
import time
from HealVnfHandler import OpenStackAPI
from PublishHandler import publisher
from threading import Thread
app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/healvnf', methods=['POST'])
def ReceiveHealVnfRequest():
    print('Receive HealVnfRequest from EM')
    data = request.get_json()
    id = data['id']
    cause = data['cause']
    name = data['name']
    #print('vnf instance id = {id} cause = {cause}'.format(id=id,cause=cause))
    #pid = os.fork()
    #if pid==0:
    def HealVnfProcessStart(id,cause,name):
        #print('child id : {}'.format(os.getpid()))
        time.sleep(2)
        publisher(id,cause,name,'notification1')
        new_item = OpenStackAPI()
        if cause == 'paused':
            result = new_item.unpause(id)
        elif cause == 'suspended':
            result = new_item.resume(id,name)
        elif cause == 'shutoff':
            result = new_item.reboot(id,name)
        publisher(id,cause,name,'notification2')
        #os.kill(os.getpid())
    thread = Thread(target=HealVnfProcessStart, kwargs={'id':id,'cause':cause,'name':name})
    thread.start()
    print('Send HealVnfResponse to EM')
    return 'succesful'
app.run(host='192.168.1.103',port=5010)
