"""Collect process information from Linux."""

from dataclasses import dataclass
from pathlib import Path

PROC_PATH = Path("/proc")

@dataclass
class ProcessInfo:
    """Basic information about a Linux process."""

    pid: int
    name: str



def get_process_ids() -> list[int]:
    """Return the process IDs currently available in /proc."""


    process_ids = []


    for entry in PROC_PATH.iterdir():
        if entry.name.isdigit():
            process_ids.append(int(entry.name))

    return process_ids


def get_process_name(pid: int) -> str | None:
    """Return the process name for a PID."""

    comm_path = PROC_PATH / str(pid) / "comm"   

    try:
        return comm_path.read_text(
            encoding="utf-8"            
        ).strip()
    except FileNotFoundError:
        return None


def get_processes() -> list[ProcessInfo]:
    """Return basic information about running processes."""

    processes: list[ProcessInfo] = []

    for pid in get_process_ids():
        process_name = get_process_name(pid)

        if process_name is None:
            continue

        processes.append(
            ProcessInfo(
                pid=pid,
                name=process_name,
            )
        )
    return processes