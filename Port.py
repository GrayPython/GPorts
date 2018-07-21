#Written by 《ERFAN》
#t.me/ErfanMAfshar

import socket,os
from datetime import datetime
def main() :
    os.system('clear')
    print("|-----------------------|")
    print("|                       |")
    print("|    [+]Port Scanner    |")
    print("|                       |")
    print("|  {00} Automatic Scan  |")
    print("|  {11} Manual Scan     |")
    print("|  {99} Exit            |")
    print("|_______________________|")
    a = input("--> ")
    def pyGreen(skk) : print("\033[92m {}\033[00m".format(skk))
    def pyRed(skk) : print("\033[91m {}\033[00m".format(skk))
    if a == "00":
        server = input("Enter your site:\n(example: www.google.com) --> ")
        ips = socket.gethostbyname(server)
        print("                                         ")
        print("-----------------------------------------")
        print("Please wait, scanning remote host: " + ips)
        print("-----------------------------------------")
        print("scanning ports in range 10 to 1024")
        print("                                         ")

        time1 = datetime.now()

        try:
            for port in range(10,1024):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((ips, port))
                if result == 0:
                    pyGreen("Port {}: 	 Open".format(port))
                sock.close()
        except:
            print("Couldn't connect to server!!")

        time2 = datetime.now()
        total = time2 - time1
        print("\nDone")
        print("Scanning Completed in: " + str(total))
        oo = input("\nPress Enter ")
        if oo == "":
            main()
    elif a == "11":
        server = input("Enter your site:\n(example: www.google.com) --> ")
        ips = socket.gethostbyname(server)
        portt = input("Enter Ports:\n(example: 21,80) --> ").split(",")
        portt = [int(p) for p in portt]
        print("                                         ")
        print("-----------------------------------------")
        print("Please wait, scanning remote host: " + ips)
        print("-----------------------------------------")
        print("                                         ")

        time1 = datetime.now()

        try:
            for port in portt:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((ips, port))
                if result == 0:
                    pyGreen("Port {}: 	 Open".format(port))
                else:
                    pyRed("Port {}:     Close".format(port))
                sock.close()

        except :
            print("Couldn't connect to server!!")

        time2 = datetime.now()
        total = time2 - time1
        print("\nDone")
        print("Scanning Completed in: " + str(total))
        oo = input("\nPress Enter ")
        if oo == "":
            main()
    else:
        print("Please select the correct option!")
        oo = input("\nPress Enter ")
        if oo == "":
            main()

if __name__ == '__main__':
    main()
