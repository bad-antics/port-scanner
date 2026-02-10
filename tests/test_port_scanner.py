import unittest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from port_scanner.config import ScanConfig
from port_scanner.core import PortResult, ScanResult, Scanner

class TestConfig(unittest.TestCase):
    def test_defaults(self):
        cfg = ScanConfig()
        self.assertEqual(cfg.threads, 200)
        self.assertIn(80, cfg.COMMON_PORTS)
        self.assertEqual(cfg.SERVICE_MAP[22], "SSH")

class TestPortResult(unittest.TestCase):
    def test_creation(self):
        r = PortResult(80, "open", "HTTP", "Apache", 0.01)
        self.assertEqual(r.port, 80)
        self.assertEqual(r.state, "open")

class TestScanResult(unittest.TestCase):
    def test_open_filter(self):
        ports = [PortResult(22, "open"), PortResult(23, "closed"), PortResult(80, "open")]
        sr = ScanResult("127.0.0.1", ports)
        self.assertEqual(len(sr.open_ports), 2)

if __name__ == "__main__":
    unittest.main()
