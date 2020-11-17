import paramiko, base64,getpass,time
from ssh_jump import ssh_jump 
def reset(ip):
    if ip=='172.24.4.111':
        print('reset upf')
        cmds = ['sudo kill $(pidof ./bin/free5gc-upfd)\n','cd /home/ubuntu/stage3/src/upf/lib/libgtp5gnl/tools\n','sudo ./gtp5g-link del upfgtp0\n','sudo rm /dev/mqueue/*\n','cd /home/ubuntu/stage3/src/upf/build\n','sudo nohup ./bin/free5gc-upfd\n','exit\n']
    elif ip=='172.24.4.102':
        print('reset amf')
        cmds = ['sudo kill $(pidof ./bin/amf)\n','cd /home/ubuntu/stage3\n','sudo nohup ./bin/amf\n','exit\n']
        #stdin,stdout,stderr = client.exec_command('sudo kill $(pidof ./bin/amf);cd /home/ubuntu/stage3;sudo ./bin/amf')
    elif ip=='172.24.4.103':
        print('reset smf')
        cmds = ['sudo kill $(pidof ./bin/smf)\n','cd /home/ubuntu/stage3\n','sudo nohup ./bin/smf\n','exit\n']
        #stdin,stdout,stderr = client.exec_command('sudo kill $(pidof ./bin/smf);cd /home/ubuntu/stage3;sudo ./bin/smf')
    elif ip=='172.24.4.104':
        print('reset udr')
        cmds = ['sudo kill $(pidof ./bin/udr)\n','cd /home/ubuntu/stage3\n','sudo nohup ./bin/udr\n','exit\n']
        #stdin,stdout,stderr = client.exec_command('sudo kill $(pidof ./bin/udr);cd /home/ubuntu/stage3;sudo ./bin/udr')
    elif ip=='172.24.4.105':
        print('reset pcf')
        cmds = ['sudo kill $(pidof ./bin/pcf)\n','cd /home/ubuntu/stage3\n','sudo nohup ./bin/pcf\n','exit\n']
        #stdin,stdout,stderr = client.exec_command('sudo kill $(pidof ./bin/pcf);cd /home/ubuntu/stage3;sudo ./bin/pcf')
    elif ip=='172.24.4.106':
        print('reset udm')
        cmds = ['sudo kill $(pidof ./bin/udm)\n','cd /home/ubuntu/stage3\n','sudo nohup ./bin/udm\n','exit\n']
        #stdin,stdout,stderr = client.exec_command('sudo kill $(pidof ./bin/udm);cd /home/ubuntu/stage3;sudo ./bin/udm')
    elif ip=='172.24.4.107':
        print('reset nssf')
        cmds = ['sudo kill $(pidof ./bin/nssf)\n','cd /home/ubuntu/stage3\n','sudo nohup ./bin/nssf\n','exit\n']
        #stdin,stdout,stderr = client.exec_command('sudo kill $(pidof ./bin/nssf);cd /home/ubuntu/stage3;sudo ./bin/nssf')
    elif ip=='172.24.4.108':
        print('reset ausf')
        cmds = ['sudo kill $(pidof ./bin/ausf)\n','cd /home/ubuntu/stage3\n','sudo nohup ./bin/ausf\n','exit\n']
        #stdin,stdout,stderr = client.exec_command('sudo kill $(pidof ./bin/ausf);cd /home/ubuntu/stage3;sudo ./bin/ausf')

    ssh_jump(ip,cmds)
    print('reset finish')
    return 