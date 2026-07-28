"""Entry point for the Linux System Monitor."""


from system_monitor.system_info import get_system_info


def main() -> None:
    """Display general information about the system."""

    system_info = get_system_info()

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


if __name__ == "__main__":
    main()