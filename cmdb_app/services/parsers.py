import re

def parse_cpu_model(line):
    return line.split(":", 1)[1].strip() if ":" in line else line

def parse_memory(line):
    nums = re.findall(r"\d+", line)
    return {
        "mem_total_mb": int(nums[0]),
        "mem_used_mb": int(nums[1]),
        "mem_free_mb": int(nums[2]),
    }

def parse_disk(line):
    cols = line.split()
    return {
        "disk_total": cols[1],
        "disk_used": cols[2],
        "disk_avail": cols[3],
        "disk_use_percent": cols[4],
    }
