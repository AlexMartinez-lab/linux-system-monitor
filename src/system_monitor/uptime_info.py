"""Collect system uptime information from Linux."""

from pathlib import Path


UPTIME_PATH = Path("/proc/uptime")


def read_uptime_seconds() -> float:
    """Return the system uptime in seconds."""

    with UPTIME_PATH.open(
        mode="r",
        encoding="utf-8",
    ) as file:
        content = file.read()


    uptime_value = content.split()[0]

    return float(uptime_value)


def convert_seconds(
        total_seconds: float,
) -> dict[str, int]:
    """Convert seconds into days, hours, minutes, and seconds."""

    remaining_seconds = int(total_seconds)

    days = remaining_seconds // 86400
    remaining_seconds %= 86400

    hours = remaining_seconds // 3600
    remaining_seconds %= 3600

    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60


    return {
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds,
    }



def get_system_uptime() -> dict[str, int]:
    """Return the current system uptime."""

    uptime_seconds = read_uptime_seconds()

    return convert_seconds(uptime_seconds)