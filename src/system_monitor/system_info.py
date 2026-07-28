"""Collect general information about the linux system."""

import platform
import socket


def get_system_info() -> dict[str, str]:
    """Return general information about the current system."""

    return {
        "hostname": socket.gethostname(),
        "operating_system": platform.system(),
        "kernel_version": platform.release(),
        "architecture": platform.machine(),
        "python_version": platform.python_version(),
    }   

