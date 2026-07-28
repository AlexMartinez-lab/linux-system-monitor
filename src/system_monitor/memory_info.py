"""Collect memory information from the Linux system."""

from pathlib import Path

MEMINFO_PATH = Path("/proc/meminfo")


def read_memory_info() -> dict[str, int]:
    """Read memory values from /proc/meminfo."""

    memory_data: dict[str, int] = {}

    with MEMINFO_PATH.open(
        mode="r",
        encoding="utf-8",
    ) as file:
        for line in file:
            key, value = line.split(":", maxsplit=1)

            value_parts = value.strip().split()

            memory_data[key] = int(value_parts[0])

    return memory_data


def kilobytes_to_gigabytes(
    kilobytes: int,
) -> float:
    """Convert kilobytes to gigabytes."""
    return kilobytes / 1024 / 1024


def get_memory_usage() -> dict[str, float]:
    """Return the current memory usage."""

    memory_info = read_memory_info()

    total_kb = memory_info["MemTotal"]
    available_kb = memory_info["MemAvailable"]
    used_kb = total_kb - available_kb

    usage_percent = used_kb / total_kb * 100

    return {
        "total_gb": kilobytes_to_gigabytes(total_kb),
        "available_gb": kilobytes_to_gigabytes(
            available_kb
        ),
        "used_gb": kilobytes_to_gigabytes(used_kb),
        "usage_percent": usage_percent,
    }