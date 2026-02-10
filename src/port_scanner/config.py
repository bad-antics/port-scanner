"""Port Scanner Configuration"""
import os

class ScanConfig:
    def __init__(self):
        self.timeout = float(os.getenv("SCAN_TIMEOUT", "2.0"))
        self.threads = int(os.getenv("SCAN_THREADS", "200"))
        self.retries = 1
        self.verbose = False
        self.output_format = "text"
    
    COMMON_PORTS = [21,22,23,25,53,80,110,111,135,139,143,161,389,443,
        445,465,514,548,587,993,995,1433,1521,2049,3306,3389,5432,
        5900,6379,8080,8443,9090,9200,27017]
    
    TOP_1000 = list(range(1, 1001))
    
    SERVICE_MAP = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
        80: "HTTP", 110: "POP3", 135: "MSRPC", 139: "NetBIOS",
        143: "IMAP", 161: "SNMP", 389: "LDAP", 443: "HTTPS",
        445: "SMB", 993: "IMAPS", 995: "POP3S", 1433: "MSSQL",
        1521: "Oracle", 3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL",
        5900: "VNC", 6379: "Redis", 8080: "HTTP-Proxy", 8443: "HTTPS-Alt",
        9090: "Prometheus", 9200: "Elasticsearch", 27017: "MongoDB",
    }
