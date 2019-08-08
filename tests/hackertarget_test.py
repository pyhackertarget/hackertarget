#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from unittest.mock import Mock
from source import hackertarget_api

class hackertarget_test(unittest.TestCase):
    def test_traceroute_script(self):
        hackertarget_api.hackertarget_api = Mock()
        hackertarget_api.hackertarget_api(1, "facebook.com")
        hackertarget_api.hackertarget_api.assert_called_once_with(1, "facebook.com")

    def test_ping_script(self):
        hackertarget_api.hackertarget_api = Mock()
        hackertarget_api.hackertarget_api(2, "facebook.com")
        hackertarget_api.hackertarget_api.assert_called_once_with(2, "facebook.com")

    def test_dns_lookup_script(self):
        hackertarget_api.hackertarget_api = Mock()
        hackertarget_api.hackertarget_api(3, "facebook.com")
        hackertarget_api.hackertarget_api.assert_called_once_with(3, "facebook.com")

    def test_reverse_dns_script(self):
        hackertarget_api.hackertarget_api = Mock()
        hackertarget_api.hackertarget_api(4, "facebook.com")
        hackertarget_api.hackertarget_api.assert_called_once_with(4, "facebook.com")

    def test_find_dns_host_script(self):
        hackertarget_api.hackertarget_api = Mock()
        hackertarget_api.hackertarget_api(5, "facebook.com")
        hackertarget_api.hackertarget_api.assert_called_once_with(5, "facebook.com")

    def test_find_shared_dns_script(self):
        hackertarget_api.hackertarget_api = Mock()
        hackertarget_api.hackertarget_api(6, "facebook.com")
        hackertarget_api.hackertarget_api.assert_called_once_with(6, "facebook.com")

    def test_zone_transfer_script(self):
        hackertarget_api.hackertarget_api = Mock()
        hackertarget_api.hackertarget_api(7, "facebook.com")
        hackertarget_api.hackertarget_api.assert_called_once_with(7, "facebook.com")

    def test_whois_lookup_script(self):
        hackertarget_api.hackertarget_api = Mock()
        hackertarget_api.hackertarget_api(8, "facebook.com")
        hackertarget_api.hackertarget_api.assert_called_once_with(8, "facebook.com")

    def test_ip_location_lookup_script(self):
        hackertarget_api.hackertarget_api = Mock()
        hackertarget_api.hackertarget_api(9, "facebook.com")
        hackertarget_api.hackertarget_api.assert_called_once_with(9, "facebook.com")

    def test_reverse_ip_lookup_script(self):
        hackertarget_api.hackertarget_api = Mock()
        hackertarget_api.hackertarget_api(10, "facebook.com")
        hackertarget_api.hackertarget_api.assert_called_once_with(10, "facebook.com")

    def test_tcp_port_scan_lookup_script(self):
        hackertarget_api.hackertarget_api = Mock()
        hackertarget_api.hackertarget_api(11, "facebook.com")
        hackertarget_api.hackertarget_api.assert_called_once_with(11, "facebook.com")

    def test_subnet_lookup_script(self):
        hackertarget_api.hackertarget_api = Mock()
        hackertarget_api.hackertarget_api(12, "facebook.com")
        hackertarget_api.hackertarget_api.assert_called_once_with(12, "facebook.com")

    def test_http_header_check_script(self):
        hackertarget_api.hackertarget_api = Mock()
        hackertarget_api.hackertarget_api(13, "facebook.com")
        hackertarget_api.hackertarget_api.assert_called_once_with(13, "facebook.com")

    def test_extract_page_links_script(self):
        hackertarget_api.hackertarget_api = Mock()
        hackertarget_api.hackertarget_api(14, "facebook.com")
        hackertarget_api.hackertarget_api.assert_called_once_with(14, "facebook.com")
