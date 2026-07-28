"""Entry point for the Linux System Monitor."""

from system_monitor.memory_info import get_memory_usage
from system_monitor.system_info import get_system_info


def main() -> None:
    """Display information about the system."""

    system_info = get_system_info()

    memory_usage = get_memory_usage()
    
    print("Linux System Monitor")
    print("======================")
    print()
    print(f"Hostname: {system_info['hostname']}")
    print(
        "Operating System: "
        f"{system_info['operating_system']}"
    )

    print(
        "Kernel Version: "
        f"{system_info['kernel_version']}"
    )

    print(f"Architecture: {system_info['architecture']}")
    print(
        "Python version: "
        f"{system_info['python_version']}"
    )

    print()
    print("Memory")
    print("======")
    print()
    print(f"Total: {memory_usage['total_gb']:.2f} GB")
    print(
        f"Available: "
        f"{memory_usage['available_gb']:.2f} GB"
    )
    print(f"Used: {memory_usage['used_gb']:.2f} GB")
    print(
        f"Usage: "
        f"{memory_usage['usage_percent']:.2f}%"
    )


if __name__ == "__main__":
    main()