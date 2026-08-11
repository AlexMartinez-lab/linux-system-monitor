"""Collect CPU usage information from Linux."""

import os
import time
from pathlib import Path


STAT_PATH = Path("/proc/stat")


def read_cpu_times() -> tuple[int, int]:
    """Return the total and idle CPU times."""

    with STAT_PATH.open(
        mode="r",
        encoding="utf-8",
    ) as file:
        first_line = file.readline()


    values  = first_line.split()

    cpu_times = [int(value) for value in values[1:]]

    idle_time = cpu_times[3] + cpu_times[4]
    total_time = sum(cpu_times)

    return total_time, idle_time


def calculate_cpu_usage(
    first_sample: tuple[int, int],
    second_sample: tuple[int, int],
) -> float:
    """Calculate CPU usage between two samples."""

    first_total, first_idle = first_sample
    second_total, second_idle = second_sample

    total_delta = second_total - first_total
    idle_delta = second_idle - first_idle

    if total_delta == 0:
        return 0.0

    active_delta = total_delta - idle_delta

    return active_delta / total_delta * 100

def get_cpu_usage(
        interval: float = 1.0,
) -> dict[str, int | float]:
    """Return current CPU usage information."""

    first_sample = read_cpu_times()

    time.sleep(interval)

    second_sample = read_cpu_times()

    usage_percent = calculate_cpu_usage(
        first_sample,
        second_sample,
    )


    logical_cpus = os.cpu_count() or 0

    return {
        "usage_percent": usage_percent,
        "logical_cpus": logical_cpus,
    }