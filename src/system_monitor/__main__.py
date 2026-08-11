"""Entry point for the Linux System Monitor."""

from system_monitor.cpu_info import get_cpu_usage
from system_monitor.disk_info import get_disk_usage
from system_monitor.memory_info import get_memory_usage
from system_monitor.system_info import get_system_info
from system_monitor.uptime_info import get_system_uptime
from system_monitor.process_info import get_processes

def main() -> None:
    """Display information about the system."""

    system_info = get_system_info()

    system_uptime = get_system_uptime()

    cpu_usage = get_cpu_usage()
    
    memory_usage = get_memory_usage()
 
    disk_usage = get_disk_usage()

    processes = get_processes()
    
    
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
    print("System Uptime")
    print("=============")
    print()
    print(
        f"{system_uptime['days']} days, "
        f"{system_uptime['hours']} hours, "
        f"{system_uptime['minutes']} minutes, "
        f"{system_uptime['seconds']} seconds"
    )

    print()
    print("CPU")
    print("===")
    print()
    print(f"Logical CPUs: {cpu_usage['logical_cpus']}")
    print(f"Usage: {cpu_usage['usage_percent']:.2f}%")

    
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


    print()
    print("Disk")
    print("====")
    print()
    print(f"Filesystem: {disk_usage['path']}")
    print(f"Total: {disk_usage['total_gib']:.2f} GiB")
    print(f"Used: {disk_usage['used_gib']:.2f} GiB")
    print(f"Free: {disk_usage['free_gib']:.2f} GiB")
    print(f"Usage: {disk_usage['usage_percent']:.2f}%")


    print()
    print("Processes")
    print("=========")
    print()
    print(f"{'PID':<8} Name")
    print("-" * 30)

    for process in processes[:10]:
        print(f"{process.pid:<8} {process.name}")

if __name__ == "__main__":
    main()