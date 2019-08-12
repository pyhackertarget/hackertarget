#!/usr/bin/env python
# -*- coding: utf-8 -*-

from source import hackertarget_api
import time

hackertarget_logo = """
  _               _              _                          _
 | |_   __ _  __ | |__ ___  _ _ | |_  __ _  _ _  __ _  ___ | |_
 | ' \ / _` |/ _|| / // -_)| '_||  _|/ _` || '_|/ _` |/ -_)|  _|
 |_||_|\__,_|\__||_\_\\___||_|   \__|\__,_||_|  \__, |\___| \__|
                                                |___/
                 Ismail Tasdelen
 | github.com/ismailtasdelen | linkedin.com/in/ismailtasdelen |
"""

menu = """
[1] Traceroute
[2] Ping Test
[3] DNS Lookup
[4] Reverse DNS
[5] Find DNS Host
[6] Find Shared DNS
[7] Zone Transfer
[8] Whois Lookup
[9] IP Location Lookup
[10] Reverse IP Lookup
[11] TCP Port Scan
[12] Subnet Lookup
[13] HTTP Header Check
[14] Extract Page Links
[15] Version
[16] Exit
"""

print(hackertarget_logo)
print(menu)

def run():

    try:
        choice = input("Which option number : ")

        if choice == '1':
            print("\n")
            print("[+] Traceroute script running..")
            target = input("[+] Target : ")
            print("\n")
            txt = hackertarget_api.hackertarget_api(1, target)
            print(txt)

        elif choice == '2':
            print("\n")
            print("[+] Ping Test script running..")
            target = input("[+] Target : ")
            print("\n")
            txt = hackertarget_api.hackertarget_api(2, target)
            print(txt)

        elif choice == '3':
            print("\n")
            print("[+] DNS Lookup script running..")
            target = input("[+] Target : ")
            print("\n")
            txt = hackertarget_api.hackertarget_api(3, target)
            print(txt)

        elif choice == '4':
            print("\n")
            print("[+] Reverse DNS script running..")
            target = input("[+] Target : ")
            print("\n")
            txt = hackertarget_api.hackertarget_api(4, target)
            print(txt)

        elif choice == '5':
            print("\n")
            print("[+] Find DNS Host script running..")
            target = input("[+] Target : ")
            print("\n")
            txt = hackertarget_api.hackertarget_api(5, target)
            print(txt)

        elif choice == '6':
            print("\n")
            print("[+] Find Shared DNS script running..")
            target = input("[+] Target : ")
            print("\n")
            txt = hackertarget_api.hackertarget_api(6, target)
            print(txt)

        elif choice == '7':
            print("\n")
            print("[+] Zone Transfer script running..")
            target = input("[+] Target : ")
            print("\n")
            txt = hackertarget_api.hackertarget_api(7, target)
            print(txt)

        elif choice == '8':
            print("\n")
            print("[+] Whois Lookup script running..")
            target = input("[+] Target : ")
            print("\n")
            txt = hackertarget_api.hackertarget_api(8, target)
            print(txt)

        elif choice == '9':
            print("\n")
            print("[+] IP Location Lookup script running..")
            target = input("[+] Target : ")
            print("\n")
            txt = hackertarget_api.hackertarget_api(9, target)
            print(txt)

        elif choice == '10':
            print("\n")
            print("[+] Reverse IP Lookup script running..")
            target = input("[+] Target : ")
            print("\n")
            txt = hackertarget_api.hackertarget_api(10, target)
            print(txt)

        elif choice == '11':
            print("\n")
            print("[+] TCP Port Scan script running..")
            target = input("[+] Target : ")
            print("\n")
            txt = hackertarget_api.hackertarget_api(11, target)
            print(txt)

        elif choice == '12':
            print("\n")
            print("[+] Subnet Lookup script running..")
            target = input("[+] Target : ")
            print("\n")
            txt = hackertarget_api.hackertarget_api(12, target)
            print(txt)

        elif choice == '13':
            print("\n")
            print("[+] HTTP Header Check script running..")
            target = input("[+] Target : ")
            print("\n")
            txt = hackertarget_api.hackertarget_api(13, target)
            print(txt)

        elif choice == '14':
            print("\n")
            print("[+] Extract Page Links script running..")
            target = input("[+] Target : ")
            print("\n")
            txt = hackertarget_api.hackertarget_api(14, target)
            print(txt)
            
        elif choice == '15':
            print("\n")
            print("[+] Version Checking..")
            time.sleep(2)
            version_number = "2.0"
            time.sleep(3)
            print("[+] Version : " + version_number)

        elif choice == '16':
            exit()

    except KeyboardInterrupt:
        print("\nAborted!")
        quit()
    except:
        print("Invalid Option !\n")
        return run()
run()
