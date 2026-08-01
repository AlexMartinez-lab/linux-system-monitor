"""Collect disk usage information from the Linux Sistem."""

import shutil


def bytes_to_gibibytes(byte_count: int) -> float:
    """Convert bytes to gibibytes."""

    return byte_count / 1024 / 1024 / 1024


def get_disk_usage(
    path: str = "/",
) -> dict[str, str | float]:
    """Return disk usage information for a filesystem path."""

    disk_usage = shutil.disk_usage(path)

    usage_percent = disk_usage.used  / disk_usage.total * 100


    return {
        "path": path,
        "total_gib": bytes_to_gibibytes(
            disk_usage.total
        ),
        "used_gib": bytes_to_gibibytes(
            disk_usage.used
        ),
        "free_gib": bytes_to_gibibytes(
            disk_usage.used
        ),
        "usage_percent": usage_percent,
    }


