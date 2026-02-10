"""Output formatters"""
import json, csv, io

def format_text(result):
    lines = [f"\nScan: {result.target} ({len(result.open_ports)} open ports)"]
    lines.append("-" * 50)
    lines.append(f"{'PORT':<8} {'STATE':<10} {'SERVICE':<15} BANNER")
    for p in result.open_ports:
        lines.append(f"{p.port:<8} {p.state:<10} {p.service:<15} {p.banner[:40]}")
    return "\n".join(lines)

def format_json(result):
    return json.dumps(result.to_dict(), indent=2)

def format_csv(result):
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["port", "state", "service", "banner"])
    for p in result.open_ports:
        w.writerow([p.port, p.state, p.service, p.banner])
    return buf.getvalue()
