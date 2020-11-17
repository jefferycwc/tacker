import multiprocessing
from multiprocessing import Process, Pool
import os
import signal
import sys
def worker(arg):
    os.system(arg)

def kill_process():
    process_name = ['mongo_detect.py','upf_detect.py','nrf_detect.py','amf_detect.py','smf_detect.py','udr_detect.py','pcf_detect.py','udm_detect.py','nssf_detect.py','ausf_detect.py','ReceiveHandler.py']
    #process_name = ['pcf_detect.py','ReceiveHandler.py']
    for process in process_name:
        #print(process)
        for line in os.popen("ps ax | grep " + process + " | grep -v grep"):
            fields = line.split()
            pid = fields[0]
            #print(pid)
            os.kill(int(pid), signal.SIGKILL)

if __name__ == "__main__":
    os.chdir("/root/fault_management/master_node")
    original_sigint_handler = signal.signal(signal.SIGINT, signal.SIG_IGN)
    pool =Pool(11)
    #pool = Pool(2)
    cmds = ["python mongo_detect.py","python upf_detect.py","python nrf_detect.py","python amf_detect.py","python smf_detect.py","python udr_detect.py","python pcf_detect.py","python udm_detect.py","python nssf_detect.py","python ausf_detect.py","python ReceiveHandler.py"]
    #cmds = ["python pcf_detect.py","python ReceiveHandler.py"]
    signal.signal(signal.SIGINT, original_sigint_handler)
    try:
        result=pool.map_async(worker,cmds).get(2000)
    except KeyboardInterrupt:
        print("Caught KeyboardInterrupt, terminating workers")
        pool.terminate()
        kill_process()
    else:
        print("Normal termination")
        pool.close()
    pool.join()
