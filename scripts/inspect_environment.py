#!/usr/bin/env python3
"""Inspect only this machine's non-secret install prerequisites."""
import json
import os
import platform
import shutil
import subprocess
from pathlib import Path


def command(args):
    try:
        p = subprocess.run(args, capture_output=True, text=True, timeout=12, errors="replace")
        return p.stdout.strip()[:4000] if p.returncode == 0 else None
    except (OSError, subprocess.TimeoutExpired):
        return None


def memory_bytes():
    try:
        if platform.system() == "Windows":
            import ctypes
            class MEMORY(ctypes.Structure):
                _fields_ = [("length", ctypes.c_ulong), ("load", ctypes.c_ulong)] + [(name, ctypes.c_ulonglong) for name in ("total_phys", "avail_phys", "total_page", "avail_page", "total_virtual", "avail_virtual", "extended")]
            m = MEMORY()
            m.length = ctypes.sizeof(m)
            if ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m)):
                return {"total": m.total_phys, "available": m.avail_phys}
        if platform.system() == "Linux":
            rows = Path("/proc/meminfo").read_text().splitlines()
            values = {row.split(":")[0]: int(row.split()[1]) * 1024 for row in rows if row.startswith(("MemTotal:", "MemAvailable:"))}
            return {"total": values.get("MemTotal"), "available": values.get("MemAvailable")}
        if platform.system() == "Darwin":
            value = command(["sysctl", "-n", "hw.memsize"])
            return {"total": int(value) if value else None, "available": None}
    except (OSError, ValueError, AttributeError):
        pass
    return None


def main():
    disk = shutil.disk_usage(Path.cwd())
    names = ["python3", "python", "node", "npm", "git", "docker", "nvidia-smi", "ollama", "ffmpeg", "adb", "winget", "brew", "google-chrome", "chromium", "msedge"]
    tools = {name: shutil.which(name) for name in names}
    gpu = command([tools["nvidia-smi"], "--query-gpu=name,memory.total,driver_version", "--format=csv,noheader"]) if tools["nvidia-smi"] else None
    result = {
        "scope": "only_the_machine_running_this_script",
        "os": platform.system(), "release": platform.release(), "architecture": platform.machine(),
        "python": platform.python_version(), "logical_cpus": os.cpu_count(), "memory_bytes": memory_bytes(),
        "disk_free_bytes_at_cwd": disk.free, "tools": tools, "nvidia_gpu": gpu,
        "notes": ["未读取密钥、Cookie、浏览器历史或完整环境变量。", "PATH 中没有浏览器不证明未安装；需要通过目标桌面/标准安装位置确认。", "未检测 GPU 不代表不存在；Apple/AMD/Intel 使用官方平台方式另查。", "未访问网络；图形会话可用性由实际交互工具确认。"]
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
