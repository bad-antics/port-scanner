"""Port Scanner Core Engine"""
import socket, threading, time, json
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

class PortResult:
    def __init__(self, port, state, service="", banner="", rtt=0.0):
        self.port = port
        self.state = state
        self.service = service
        self.banner = banner
        self.rtt = rtt

class ScanResult:
    def __init__(self, target, ports):
        self.target = target
        self.ports = ports
        self.timestamp = datetime.now()
        self.open_ports = [p for p in ports if p.state == "open"]
    
    def to_dict(self):
        return {"target": self.target, "open_ports": len(self.open_ports),
                "ports": [{"port": p.port, "state": p.state, "service": p.service, "banner": p.banner} for p in self.open_ports]}

class Scanner:
    def __init__(self, config):
        self.config = config
    
    def scan_port(self, host, port):
        service = self.config.SERVICE_MAP.get(port, "unknown")
        start = time.time()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.config.timeout)
            result = sock.connect_ex((host, port))
            rtt = time.time() - start
            if result == 0:
                banner = self._grab_banner(sock)
                sock.close()
                return PortResult(port, "open", service, banner, rtt)
            sock.close()
            return PortResult(port, "closed", service, "", rtt)
        except socket.timeout:
            return PortResult(port, "filtered", service, "", time.time() - start)
        except:
            return PortResult(port, "error", service)
    
    def scan_host(self, host, ports=None):
        ports = ports or self.config.COMMON_PORTS
        results = []
        with ThreadPoolExecutor(max_workers=self.config.threads) as executor:
            futures = {executor.submit(self.scan_port, host, p): p for p in ports}
            for future in as_completed(futures):
                results.append(future.result())
        results.sort(key=lambda r: r.port)
        return ScanResult(host, results)
    
    def _grab_banner(self, sock):
        try:
            sock.settimeout(1.5)
            return sock.recv(1024).decode(errors="ignore").strip()[:200]
        except: return ""
    
    def scan_range(self, host, start_port=1, end_port=1024):
        return self.scan_host(host, list(range(start_port, end_port + 1)))
