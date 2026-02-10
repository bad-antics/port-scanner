"""Service and version detection"""
import re

VERSION_PATTERNS = {
    "SSH": re.compile(r"SSH-[\d.]+-(.+)"),
    "Apache": re.compile(r"Apache/([\d.]+)"),
    "nginx": re.compile(r"nginx/([\d.]+)"),
    "OpenSSH": re.compile(r"OpenSSH_([\d.]+)"),
    "FTP": re.compile(r"220[- ](.+)"),
    "SMTP": re.compile(r"220[- ](.+)"),
}

def detect_service(banner):
    for name, pattern in VERSION_PATTERNS.items():
        m = pattern.search(banner)
        if m:
            return {"service": name, "version": m.group(1)}
    return {"service": "unknown", "version": ""}

def fingerprint_os(open_ports):
    port_set = {p.port for p in open_ports}
    if 3389 in port_set or 445 in port_set:
        return "Windows"
    elif 22 in port_set and 135 not in port_set:
        return "Linux/Unix"
    return "Unknown"
