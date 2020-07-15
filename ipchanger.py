import time
import os
import requests

os.system("clear")
def ma_ip():
    url='https://www.myexternalip.com/raw'
    get_ip= requests.get(url,proxies=dict(http='socks5://127.0.0.1:9050',
                                 https='socks5://127.0.0.1:9050'))
    return get_ip.text

def change():
    os.system("service tor reload")
    print ('<<<<<<<<<<<<<<<<Your IP has been Changed>>>>>>>>>>>>>>>>> '+str(ma_ip()))

print('''\033[1;32;40m \n

____ _  _ ____ _  _ _   _ _  _ ____ _  _ ____    ___  _  _ _ _    _ ___  ___  _ _  _ ____ ____ 
|__| |\ | |  | |\ |  \_/  |\/| |  | |  | [__     |__] |__| | |    | |__] |__] | |\ | |___ [__  
|  | | \| |__| | \|   |   |  | |__| |__| ___]    |    |  | | |___ | |    |    | | \| |___ ___] 
                                                                                               

_ ___     ____ _  _ ____ _  _ ____ ____ ____    ___  _   _    ___ ____ ____ ____ ____ ____ _  _ 
| |__]    |    |__| |__| |\ | | __ |___ |__/    |__]  \_/      |  |__| [__  |__| |__/ |  | |  | 
| |       |___ |  | |  | | \| |__] |___ |  \    |__]   |       |  |  | ___] |  | |  \ |__|  \/                                                        



''')
print("\033[1;40;31m http://facebook.com/tasarov.tasarov.7/\n")

print("\033[1;40;31m Yes... I am a CRIMINAL. My crime is that of CURIOSITY.\n")

print("\033[1;40;31m Install ka muna ng TOR atsaka PRIVOXY, pag di ka marunong tangina mo mag ARAL ka muna! - TASAROV\n")

os.system("service tor start")




time.sleep(5)
print("\033[1;32;40m change your  SOCKS to 127.0.0.1:9050 \n")
os.system("service tor start")
x = input("time to change Ip in Sec [type=60] >> ")
lin = input("how many time do you want to change your ip [type=1000]for infinte ip change type [0] >>")
if str(lin) =='0':

	while True:
		try:
			time.sleep(int(x))
			change()
		except KeyboardInterrupt:

		 	print('auto tor is closed ')
		 	quit()

else:


	for i in range(int(lin)):
		    time.sleep(int(x))
		    change()
