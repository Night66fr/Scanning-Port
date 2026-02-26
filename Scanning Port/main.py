# Scanning for port 
import socket
import concurrent.futures

def ip_ask():
    # input ip
    print('Ip format : x.x.x.x')
    print('Each x is between 1 to 3')
    ip_chosen = input('What ip do you want to scan ? (ipv4)\n')
    return ip_chosen

def port_try():
    # tcp connection  = open
    # no tcp connection = close
    port_chosen = input('Do you want to enter a specific port ? (enter to skip and scan all)\n')
    if port_chosen == '':
        port_chosen = port_chosen
    else:
        port_chosen = int(port_chosen)
    return port_chosen
    

def open_close(ip_chosen, port_chosen):
    test_port = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    test_port.settimeout(0.5)
    test_port_result = test_port.connect_ex((ip_chosen, port_chosen))
    if test_port_result == 0:
        print(f'Port {port_chosen} is open')
        test_port.close()
        return 0
    else:
        #print(f'Port {port_chosen} is closed') # Commented out to avoid spamming the console
        test_port.close() 
        return 1


# loop 1 to 1024
def main():
    target_address = ip_ask()
    target_port = port_try()
    ouvert = 0
    ferme = 0

    print(f'You chose to scan the ip address : {target_address}')

    if target_port == '':
        with concurrent.futures.ThreadPoolExecutor(max_workers=250) as executor:
            liste_tickets = []
            for port in range(1, 1025):
                futures = [executor.submit(open_close, target_address, port)]
                liste_tickets.append(futures)
            for i in liste_tickets:
                for f in concurrent.futures.as_completed(i):
                    resultat = f.result()
                    if resultat == 0:
                        ouvert += 1
                    else:
                        ferme += 1
        print('You chose not to put any port')
        print('The scan of all ports has begun')

    else:
        print(f'You chose to scan the port : {target_port}')
        resultat = open_close(target_address, target_port)
        if resultat == 0:
            ouvert += 1
        else:
            ferme += 1

    print(f"There are {ouvert} open ports and {ferme} closed ports")

main()