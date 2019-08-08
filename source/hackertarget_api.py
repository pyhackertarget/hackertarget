#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
