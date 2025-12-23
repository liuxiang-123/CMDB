from .ssh_client import SSHClient
from .parsers import parse_cpu_model, parse_memory, parse_disk

def discover_server(host, username, password):
    client = SSHClient(host, username, password)
    result = {"host": host, "success": False}

    try:
        client.connect()

        raw = {
            "hostname": client.run("hostname").strip(),
            "os": client.run("uname -a").strip(),
            "cpu": client.run("lscpu | grep 'Model name'").strip(),
            "memory": client.run("free -m | grep Mem").strip(),
            "disk": client.run("df -h --total | grep total").strip(),
        }

        result["data_structured"] = {
            "hostname": raw["hostname"],
            "os": raw["os"],
            "cpu_model": parse_cpu_model(raw["cpu"]),
            **parse_memory(raw["memory"]),
            **parse_disk(raw["disk"]),
        }

        result["success"] = True

    except Exception as e:
        result["error"] = str(e)

    finally:
        client.close()

    return result

from django.utils import timezone
from cmdb_app.models import AssetServer

def save_discovery_to_db(ip: str, data: dict) -> AssetServer:
    obj, _ = AssetServer.objects.update_or_create(
        ip=ip,
        defaults={
            "hostname": data.get("hostname", ""),
            "os": data.get("os", ""),
            "cpu_model": data.get("cpu_model", ""),
            "mem_total_mb": data.get("mem_total_mb"),
            "mem_used_mb": data.get("mem_used_mb"),
            "mem_free_mb": data.get("mem_free_mb"),
            "disk_total": data.get("disk_total", ""),
            "disk_used": data.get("disk_used", ""),
            "disk_avail": data.get("disk_avail", ""),
            "disk_use_percent": data.get("disk_use_percent", ""),
            "status": "online",
            "last_discovered_at": timezone.now(),
        }
    )
    return obj
