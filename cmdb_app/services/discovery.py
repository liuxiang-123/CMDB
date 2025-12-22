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
