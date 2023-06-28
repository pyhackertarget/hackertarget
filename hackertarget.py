#!/usr/bin/env python
# -*- coding: utf-8 -*-

from source import hackertarget_api
import time

hackertarget_logo = """
Opentracker
Best Online IP Tracker
154.36.128.0
 Click to search!
Summary of IP's Profile DetailsCopy
IP address: 154.36.128.0
City: Saratoga
Region name: California
Country name: United States
Life Expectency: 77.1
Avg income: 30,575 USD
Timezone: America/Los_Angeles
Sub continent: North America
Country code: US
Geo-targeting: true
   ◉ Latitude: 37.751
   ◎ Longitude: -97.822
World currency: USD
EU member: false
org: Hong Kong Megalayer Technology Co.,Limited
isp: Hong Kong Megalayer Technology Co.,Limited
Connection: Cable/DSL
Continent: North America
Population: 278,357,000
IP range tracked: 154.36.0.0 - 154.42.71.255
Surface area: 9,363,520 km sq.
GNP: 8,510,700 mln.
Demographic data: true
Ad (re)targeting: true



The Ultimate IP Address Tracker.
Identify users, collect online details, get IP numbers. View, download and process enriched ip tracker data.

Do you need an IP tracker, to collect user profiles to your website and online assets, based on IP addresses? Need to find out what a visitor from a specific IP address did? Need to track whats working well for your business and what needs to be improved?

This is possible, using our IP tracking technology.

Our reporting system keeps track of every visitor, prospect or customer who visits your online assets, based on IP addresses. Get access to a complete record of activity-per-visit. Improve your business by tracking. All winners are trackers.

What Is An IP Address?
An IP address (Internet Protocol address) is a unique numerical label assigned to a device. It provides the location of the device in a network and a route on how to get there. The internet uses an IP address to send IP packets from a source to a destination. It is a building block that lets the internet function.

Can an IP address identify me?
No, an ip address does not reveal personal information (like a name, social security number or physical address). Millions of devices, like modems and routers keep logs of ip addresses.  Your modem at home, or the 4G antennae you connect to with your phone are logging your ip  addresses. Logs are necessary to maintain the internet. Logs with IP addresses are everywhere!
 
A device keeping track of an ip address.

 A device keeping track of an ip address.

Can I track someones IP-address ?
No, you can’t just track an Ip-address. You first need to have received one. Compare it to receiving a letter. If you receive the letter, then you can figure out where the letter came from by looking at the return address. If you don’t have the letter, then you also won’t have a return address. By the same token, if a letter does not have a destination address, you will not get a letter, and there is nothing to track it back to.

In internet terms this means you need a source address, a destination address and traffic (an email or a browser action) between the two. Normally an online business has a site or app as the destination and someone surfing the web is the source. If you are a business that has a site or an app and you are receiving internet traffic to the site or app the you will be able to see the ip-addresses coming to your site or app. Other places you can also see ip addresses are in the headers of the emails you receive or the log files of routers.

How does an IP tracker work?
Use the IP tracker with an IP address to identify and collect online details based on the IP number. Advanced technology combined with cookies allows you to identify visitors. Enrich, view, download and process IP tracker data with Opentracker.

Opentracker records each unique user and their IP address. Our IP tracer maps where an IP address (and the visitor behind it) originates from, and enriches this data with different sources.

Do you need to find a specific user or visitor?
Your business can locate any user or unique visitor who has been on your website by IP address.

Go back through your historical data to see entire visit or session history of any IP address. 

Can I tag IP addresses?
Yes, Opentracker allows businesses to automatically or manually tag any ip address for future reference, or processing to other destinations.

Can I investigating click-fraud?
Yes, detect Click-fraud and provide proof where needed.

Can I following up on a leads?
Yes, search visitors & clickstreams by IP address – make a record, enter into SalesForce, or any other CRM. Know what your (potential) clients are thinking, and what they are interested in. See how often a potential leads or clients returns, along with their entire history of clicks, downloads, events, and activity.

Profit from invaluable strategic insights. Improve your funnels.
Measure your prospects and customers across complex funnels. Find bottlenecks and fix them. Increase conversions and create scalable ROI.
 
 
Identify multiple customers behind a single IP address
Our first-party cookie tracking technology allows us to identify multiple customers in the same company or organization located behind the same IP address / firewall. See when your product or service offerings are passed on for consideration or discussion within an organization. 

Details about an IP address include:
Referrer, Exit, search term
Browser name & Version
Platform & Devices
Country, Region, City
GPS Longitude & Latitude
Timezone & Language
ISP, Provider or Carrier
Company & Organization
Area, Postal or ZIP code
IP address & Connection type
Display size & Orientation
ABOUT US
Opentracker has more than 10 years experience in tracking, data analytics and statistics innovation. Our hallmark is simple, intuitive, and easy-to-read reporting interfaces, combined with powerful and flexible APIs.
QUICK LINKS
Products video
Features
Pricing
Resources
Articles
Company
Login
Contact
Terms
Privacy
OT4 login
RESOURCES
Getting started
How does user-tracking work?
What is a website tracking system?
Technical Requirements Analytics
Downloadable brochures & leaflets
CONTACT
support@opentracker.net
Opentracker
Torenallee 45 - 7.17
5617 BA Eindhoven
The Netherlands
Copyright © 2023 Opentracker. All rights reserved.




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
