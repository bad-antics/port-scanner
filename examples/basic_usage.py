#!/usr/bin/env python3
from port_scanner.config import ScanConfig
from port_scanner.core import Scanner
from port_scanner.output import format_text

config = ScanConfig()
scanner = Scanner(config)

result = scanner.scan_host("scanme.nmap.org", ports=[22, 80, 443, 8080])
print(format_text(result))
