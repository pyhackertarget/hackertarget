#!/usr/bin/env python
# -*- coding: utf-8 -*-157.230.161.221
Location:

United States (US),
N/A
Region:
California (5332921)
City:
Santa Clara
ZIP:
95051
Hostname:
do.markupgrade.com → 157.230.161.221
IP range:
157.230.128.0 - 157.230.191.255
ISP:
Digital Ocean
Organization:
Digital Ocean
Property 	Format 	Description
success 	Boolean 	true if the API request was successful, false if otherwise.
approved_senders 	Array 	Approved senders that match given criteria
total 	Integer 	Total count of approved senders that match given criteria
pagination 	String 	Human readable pagination details
total_pages 	Integer 	Total number of pages
links 	Array 	An array containing links to the first page, last page, next page, and previous page of records ("next" and "previous" will only appear in the array when they are applicable). These URLs are also available in the return headers. 
import requests

def hackertarget_api(choice, target):
    request_urls = [
        "https://api.hackertarget.com/mtr/?q=",
        "https://api.hackertarget.com/nping/?q=",
        "https://api.hackertarget.com/dnslookup/?q=",
        "https://api.hackertarget.com/reversedns/?q=",
        "https://api.hackertarget.com/hostsearch/?q=",
        "https://api.hackertarget.com/findshareddns/?q=",
        "https://api.hackertarget.com/zonetransfer/?q=",
        "https://api.hackertarget.com/whois/?q=",
        "https://api.hackertarget.com/geoip/?q=",
        "https://api.hackertarget.com/reverseiplookup/?q=",
        "https://api.hackertarget.com/nmap/?q=",
        "https://api.hackertarget.com/subnetcalc/?q=",
        "https://api.hackertarget.com/httpheaders/?q=",
        "https://api.hackertarget.com/pagelinks/?q=",
    ]

    request_url = request_urls[choice-1]
    url = request_url + target
    request = requests.get(url)

    return request.text
