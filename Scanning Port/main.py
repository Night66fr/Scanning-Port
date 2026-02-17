# Scanning for port 

def ip_ask():
    #input ip
    print('Ip format : x.x.x.x')
    print('Each x is between 1 to 3')
    ip_chosen = input('What ip do you want to scan ? (ipv4)\n')
    print(f'You chose to scan the ip address : {ip_chosen}')
    return ip_chosen

def port_try():
    # tcp connection  = open
    # no tcp connection = close
    x = input('Do you want to enter a specific port ? (enter to skip)\n')
    if x == '':
        print('You chose not to put any port')
    else:
        print(f'You chose to scan the port : {x}')

def open_close():
    pass

# loop 1 to 1024

address = ip_ask()
print(f'The ip chosen in the fonction is {address}')
port_try()
open_close()