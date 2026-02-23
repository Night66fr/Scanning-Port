# Scanning for port 
import socket

def ip_ask():
    #input ip
    print('Ip format : x.x.x.x')
    print('Each x is between 1 to 3')
    ip_chosen = input('What ip do you want to scan ? (ipv4)\n')
    return ip_chosen

def port_try():
    # tcp connection  = open
    # no tcp connection = close
    port_chosen = input('Do you want to enter a specific port ? (enter to skip)\n')
    return port_chosen
    

def open_close():
    pass

# loop 1 to 1024
def main():
    target_address = ip_ask()
    target_port = port_try()
    print(f'You chose to scan the ip address : {target_address}')
    if target_port == '':
        print('You chose not to put any port')
    else:
        print(f'You chose to scan the port : {target_port}')
    open_close()

main()