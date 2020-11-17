import os
import paramiko
import time
def ssh_jump(target_addr,cmds):
    key=paramiko.RSAKey.from_private_key_file('./free5gc.key')

    jumpbox=paramiko.SSHClient()
    jumpbox.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    jumpbox.connect('192.168.1.77', username='jeffery', password='jeffery71')

    jumpbox_transport = jumpbox.get_transport()
    src_addr = ('192.168.1.77', 22)
    dest_addr = (target_addr, 22)
    jumpbox_channel = jumpbox_transport.open_channel("direct-tcpip", dest_addr, src_addr)

    target=paramiko.SSHClient()
    target.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    target.connect(target_addr, username='ubuntu', pkey=key, sock=jumpbox_channel)
    ssh = target.invoke_shell()
    for cmd in cmds:
        if cmd=='sudo nohup ./bin/free5gc-upfd\n':
            time.sleep(20)
        elif cmd=='sudo make install\n':
            time.sleep(20)
        else:
            time.sleep(1)
        ssh.send(cmd)
        #out=ssh.recv(1024)
        #print(out)
    time.sleep(1)

    target.close()
    jumpbox.close()

